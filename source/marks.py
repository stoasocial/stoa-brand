# Stoa's marks: one geometry, drawn as SVG.
#   python3 source/marks.py   (needs fonttools and brotli: pip install fonttools brotli)
# Writes logos/ and favicons/. The PNG icons are the favicon-tile-*.svg and
# app-icon.svg drawings rendered at their own size in a browser.
import json, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = sys.argv[1] if len(sys.argv) > 1 else str(ROOT)
INK, PATINA = "#1d2422", "#2f7d6d"
INK_D, PATINA_D = "#e5ebe8", "#5fb8a3"
WHITE = "#ffffff"

# The master mark on a 32 grid: a speech bubble with a stoa inside it, a
# lintel on three columns on a step. The stoa is cut out of the bubble, so
# the ground shows through it; the mark is one color.
BOX = (2, 3, 28, 26)  # the mark's extent: 28 wide, 26 tall
BODY = (2, 3, 28, 21, 3.5)  # the bubble: x, y, width, height, corner radius
TAIL = [(7, 24), (7, 29), (12, 24)]  # its tail, below the left of the body, at 45°
LINTEL = (6, 7, 20, 2.5)
STEP = (5, 19.5, 22, 1.5)
# A column: its capital flares from 3.6 wide to 2.4 in a unit, then the shaft widens to 2.8 at its foot.
COLUMNS = (10, 16, 22)
CAPITAL, NECK, FOOT = (10.25, 1.8), (11.25, 1.2), (18.75, 1.4)  # (y, half width)

def fmt(v):
    return ("%.3f" % v).rstrip("0").rstrip(".")

def mark(fill, dx=0, dy=0, s=1):
    """The mark as one path, its stoa a hole (evenodd)."""
    X = lambda x: fmt((x + dx) * s); Y = lambda y: fmt((y + dy) * s)
    x, y, w, h, r = BODY
    d = (f"M{X(x+r)} {Y(y)}H{X(x+w-r)}A{fmt(r*s)} {fmt(r*s)} 0 0 1 {X(x+w)} {Y(y+r)}V{Y(y+h-r)}"
         f"A{fmt(r*s)} {fmt(r*s)} 0 0 1 {X(x+w-r)} {Y(y+h)}H{X(TAIL[2][0])}L{X(TAIL[1][0])} {Y(TAIL[1][1])}V{Y(y+h)}"
         f"H{X(x+r)}A{fmt(r*s)} {fmt(r*s)} 0 0 1 {X(x)} {Y(y+h-r)}V{Y(y+r)}A{fmt(r*s)} {fmt(r*s)} 0 0 1 {X(x+r)} {Y(y)}Z")
    for rx, ry, rw, rh in (LINTEL, STEP):
        d += f"M{X(rx)} {Y(ry)}H{X(rx+rw)}V{Y(ry+rh)}H{X(rx)}Z"
    for c in COLUMNS:
        (y0, a), (y1, b), (y2, f) = CAPITAL, NECK, FOOT
        d += f"M{X(c-a)} {Y(y0)}H{X(c+a)}L{X(c+b)} {Y(y1)}L{X(c+f)} {Y(y2)}H{X(c-f)}L{X(c-b)} {Y(y1)}Z"
    return f'<path fill="{fill}" fill-rule="evenodd" d="{d}"/>'

def svg(w, h, body, title, top=0.0, bottom=0.0):
    # top, bottom: room for the letters' overshoot past the cap line and baseline
    vh = h + top + bottom
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {fmt(-top)} {fmt(w)} {fmt(vh)}" width="{fmt(w)}" height="{fmt(vh)}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n'

# The wordmark: Spectral SemiBold, outlined, cap height = the bubble's height,
# its baseline on the bubble's bottom: the tail hangs below like a descender.
font = TTFont(str(ROOT / "fonts/spectral-600.woff2"))
gs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
CAP = font["OS/2"].sCapHeight  # 660 of 1000

def word(text, scale, x0, baseline, fill):
    pen = SVGPathPen(gs)
    x = 0
    for ch in text:
        g = cmap[ord(ch)]
        gs[g].draw(TransformPen(pen, (scale, 0, 0, -scale, x0 + x * scale, baseline)))
        x += hmtx[g][0]
    lsb = hmtx[cmap[ord(text[0])]][1]
    last = cmap[ord(text[-1])]
    adv_last = hmtx[last][0]; rsb = adv_last - (gs[last].width and adv_last) # advance only
    return f'<path fill="{fill}" d="{pen.getCommands()}"/>', x * scale, lsb * scale

H = 26.0                      # mark height on the 32 grid
B = BODY[3]                   # the bubble's height: the wordmark's cap height
SC = B / CAP                  # font units -> grid units
GAP = 6.0                     # mark to wordmark: twice the bubble's margin below the step

def wordmark_width():
    _, w, lsb = word("Stoa", SC, 0, 0, INK)
    return w, lsb

WW, LSB = wordmark_width()
from fontTools.pens.boundsPen import BoundsPen
_b = BoundsPen(gs)
for ch in "Stoa": gs[cmap[ord(ch)]].draw(_b)  # overlapping is fine: only y matters
OVER_TOP = max(0, (_b.bounds[3] - CAP) * SC)
OVER_BOTTOM = max(0, -_b.bounds[1] * SC)

def lockup(ink, patina):
    # mark at (0,0)-(28,26); wordmark baseline on the bubble's bottom
    body = mark(patina, dx=-2, dy=-3)
    path, w, lsb = word("Stoa", SC, 28 + GAP - LSB, B, ink)
    return 28 + GAP - LSB + w, H, body + path

def stacked(ink, patina):
    width = max(28, WW - LSB)
    mx = (width - 28) / 2
    body = mark(patina, dx=-2 + mx, dy=-3)
    wx = (width - (WW - LSB)) / 2 - LSB
    path, _, _ = word("Stoa", SC, wx, H + GAP + B, ink)
    return width, H + GAP + B, body + path

files = {}
w, h, b = lockup(INK, PATINA); files["stoa-lockup.svg"] = svg(w, h, b, "Stoa", OVER_TOP, OVER_BOTTOM)
w, h, b = lockup(INK_D, PATINA_D); files["stoa-lockup-reversed.svg"] = svg(w, h, b, "Stoa", OVER_TOP, OVER_BOTTOM)
w, h, b = lockup(WHITE, WHITE); files["stoa-lockup-white.svg"] = svg(w, h, b, "Stoa", OVER_TOP, OVER_BOTTOM)
w, h, b = stacked(INK, PATINA); files["stoa-lockup-stacked.svg"] = svg(w, h, b, "Stoa", 0, OVER_BOTTOM)
w, h, b = stacked(INK_D, PATINA_D); files["stoa-lockup-stacked-reversed.svg"] = svg(w, h, b, "Stoa", 0, OVER_BOTTOM)
files["stoa-mark.svg"] = svg(28, 26, mark(PATINA, -2, -3), "Stoa")
files["stoa-mark-reversed.svg"] = svg(28, 26, mark(PATINA_D, -2, -3), "Stoa")
files["stoa-mark-ink.svg"] = svg(28, 26, mark(INK, -2, -3), "Stoa")
files["stoa-mark-white.svg"] = svg(28, 26, mark(WHITE, -2, -3), "Stoa")
p, ww, lsb = word("Stoa", SC, -LSB, B, INK)
files["stoa-wordmark.svg"] = svg(ww - LSB, B, p, "Stoa", OVER_TOP, OVER_BOTTOM)

# Small sizes: a 16-pixel drawing on whole pixels: the bubble, a lintel,
# three straight columns, a step.
SMALL_BODY = "M3 1H13A2 2 0 0 1 15 3V10A2 2 0 0 1 13 12H7L4 15V12H3A2 2 0 0 1 1 10V3A2 2 0 0 1 3 1Z"
SMALL_HOLES = [(3, 3, 10, 1)] + [(x, 5, 2, 4) for x in (4, 7, 10)] + [(3, 10, 10, 1)]
def small(fill):
    holes = "".join(f"M{x} {y}h{w}v{h}h{-w}Z" for x, y, w, h in SMALL_HOLES)
    return f'<path fill="{fill}" fill-rule="evenodd" d="{SMALL_BODY}{holes}"/>'

files["favicon.svg"] = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><title>Stoa</title>'
    '<style>path{fill:%s}@media (prefers-color-scheme:dark){path{fill:%s}}</style>' % (PATINA, PATINA_D)
    + small("currentColor").replace(' fill="currentColor"', '') + "</svg>\n")
files["stoa-mark-16.svg"] = svg(16, 16, small(PATINA), "Stoa")

# The app icon: the mark in white on a patina square; full bleed, so platforms round it.
def tile(size, share=0.56, rx=0):
    s = size * share / 28          # the mark spans 56% of the tile: inside the maskable 80% circle
    dx = (size - 28 * s) / 2 / s - 2
    dy = (size - 26 * s) / 2 / s - 3
    corner = f' rx="{fmt(rx)}"' if rx else ""
    return svg(size, size, f'<rect width="{size}" height="{size}"{corner} fill="{PATINA}"/>' + mark(WHITE, dx, dy, s), "Stoa")
files["app-icon.svg"] = tile(512)
# Tab icons in PNG: the white mark on a rounded patina tile.
files["favicon-tile-32.svg"] = tile(32, 0.8, 6)
files["favicon-tile-16.svg"] = svg(16, 16, f'<rect width="16" height="16" rx="3" fill="{PATINA}"/>' + small(WHITE), "Stoa")

for name, text in files.items():
    folder = pathlib.Path(OUT) / ("logos" if name.startswith("stoa-") else "favicons")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / name).write_text(text)
print(json.dumps({"over": [OVER_TOP, OVER_BOTTOM], "wordmark_width": WW - LSB, "lockup": lockup(INK, PATINA)[:2], "stacked": stacked(INK, PATINA)[:2]}))
