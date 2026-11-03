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

# The master mark on a 32 grid: a flat roof, four columns, a base.
ROOF = (2, 3, 28, 4)
COLS = [(x, 9, 3, 14) for x in (4, 11, 18, 25)]
BASE = (2, 25, 28, 4)
BOX = (2, 3, 28, 26)  # the mark's extent: 28 wide, 26 tall

def rect(r, fill, dx=0, dy=0, s=1):
    x, y, w, h = r
    return f'<rect x="{fmt((x+dx)*s)}" y="{fmt((y+dy)*s)}" width="{fmt(w*s)}" height="{fmt(h*s)}" fill="{fill}"/>'

def fmt(v):
    return ("%.3f" % v).rstrip("0").rstrip(".")

def mark(roof, rest, dx=0, dy=0, s=1):
    return rect(ROOF, roof, dx, dy, s) + "".join(rect(c, rest, dx, dy, s) for c in COLS) + rect(BASE, rest, dx, dy, s)

def svg(w, h, body, title, top=0.0, bottom=0.0):
    # top, bottom: room for the letters' overshoot past the cap line and baseline
    vh = h + top + bottom
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {fmt(-top)} {fmt(w)} {fmt(vh)}" width="{fmt(w)}" height="{fmt(vh)}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n'

# The wordmark: Spectral SemiBold, outlined, cap height = the mark's height.
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
SC = H / CAP                  # font units -> grid units
R = 4.0                       # one roof: the unit of clear space and gaps
GAP = 2 * R                   # mark to wordmark

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
    # mark at (0,0)-(28,26); wordmark baseline on the base's bottom
    body = mark(patina, ink, dx=-2, dy=-3)
    path, w, lsb = word("Stoa", SC, 28 + GAP - LSB, H, ink)
    return 28 + GAP - LSB + w, H, body + path

def stacked(ink, patina):
    width = max(28, WW - LSB)
    mx = (width - 28) / 2
    body = mark(patina, ink, dx=-2 + mx, dy=-3)
    wx = (width - (WW - LSB)) / 2 - LSB
    path, _, _ = word("Stoa", SC, wx, H + GAP + H, ink)
    return width, H + GAP + H, body + path

files = {}
w, h, b = lockup(INK, PATINA); files["stoa-lockup.svg"] = svg(w, h, b, "Stoa", OVER_TOP, OVER_BOTTOM)
w, h, b = lockup(INK_D, PATINA_D); files["stoa-lockup-reversed.svg"] = svg(w, h, b, "Stoa", OVER_TOP, OVER_BOTTOM)
w, h, b = lockup(WHITE, WHITE); files["stoa-lockup-white.svg"] = svg(w, h, b, "Stoa", OVER_TOP, OVER_BOTTOM)
w, h, b = stacked(INK, PATINA); files["stoa-lockup-stacked.svg"] = svg(w, h, b, "Stoa", 0, OVER_BOTTOM)
w, h, b = stacked(INK_D, PATINA_D); files["stoa-lockup-stacked-reversed.svg"] = svg(w, h, b, "Stoa", 0, OVER_BOTTOM)
files["stoa-mark.svg"] = svg(28, 26, mark(PATINA, INK, -2, -3), "Stoa")
files["stoa-mark-reversed.svg"] = svg(28, 26, mark(PATINA_D, INK_D, -2, -3), "Stoa")
files["stoa-mark-ink.svg"] = svg(28, 26, mark(INK, INK, -2, -3), "Stoa")
files["stoa-mark-white.svg"] = svg(28, 26, mark(WHITE, WHITE, -2, -3), "Stoa")
p, ww, lsb = word("Stoa", SC, -LSB, H, INK)
files["stoa-wordmark.svg"] = svg(ww - LSB, H, p, "Stoa", OVER_TOP, OVER_BOTTOM)

# Small sizes: a 16-pixel drawing with three columns, on whole pixels.
def small(roof, rest):
    r = [(1, 2, 14, 2, roof)] + [(x, 5, 2, 6, rest) for x in (3, 7, 11)] + [(1, 12, 14, 2, rest)]
    return "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{f}"/>' for x, y, w, h, f in r)

files["favicon.svg"] = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><title>Stoa</title>'
    '<style>.r{fill:%s}.c{fill:%s}@media (prefers-color-scheme:dark){.r{fill:%s}.c{fill:%s}}</style>' % (PATINA, INK, PATINA_D, INK_D)
    + small("x", "x").replace('fill="x"', 'class="c"').replace('class="c"', 'class="r"', 1) + "</svg>\n")
files["stoa-mark-16.svg"] = svg(16, 16, small(PATINA, INK), "Stoa")

# The app icon: the mark in white on a patina square; full bleed, so platforms round it.
def tile(size):
    s = size * 0.56 / 28          # the mark spans 56% of the tile: inside the maskable 80% circle
    dx = (size - 28 * s) / 2 / s - 2
    dy = (size - 26 * s) / 2 / s - 3
    return svg(size, size, f'<rect width="{size}" height="{size}" fill="{PATINA}"/>' + mark(WHITE, WHITE, dx, dy, s), "Stoa")
files["app-icon.svg"] = tile(512)
# Tab icons in PNG: the tile, drawn on whole pixels at 16 and 32.
files["favicon-tile-16.svg"] = svg(16, 16, f'<rect width="16" height="16" rx="3" fill="{PATINA}"/>' +
    "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{WHITE}"/>' for x, y, w, h in
            [(2, 3, 12, 2)] + [(xx, 6, 2, 5) for xx in (4, 7, 10)] + [(2, 12, 12, 1)]), "Stoa")
files["favicon-tile-32.svg"] = svg(32, 32, f'<rect width="32" height="32" rx="6" fill="{PATINA}"/>' +
    "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{WHITE}"/>' for x, y, w, h in
            [(5, 7, 22, 3)] + [(xx, 12, 2, 9) for xx in (7, 12, 18, 23)] + [(5, 23, 22, 3)]), "Stoa")

for name, text in files.items():
    folder = pathlib.Path(OUT) / ("logos" if name.startswith("stoa-") else "favicons")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / name).write_text(text)
print(json.dumps({"over": [OVER_TOP, OVER_BOTTOM], "wordmark_width": WW - LSB, "lockup": lockup(INK, PATINA)[:2], "stacked": stacked(INK, PATINA)[:2]}))
