# Logo

The mark is a speech bubble with a stoa inside it: a lintel on three columns, standing on a step. A stoa was the covered colonnade of a Greek city where anyone could walk in and speak, and the bubble says what happens there. The bubble is Patina; the stoa is cut out of it, so the ground shows through. It is one color, so it reads the same on every ground.

## The suite

![The logo suite](images/logo-suite.png)

![The logo suite on a dark page](images/logo-suite-dark.png)

| File | What it is | Use it |
|---|---|---|
| [`stoa-lockup.svg`](../logos/stoa-lockup.svg) | **Primary logo**: the mark, then the wordmark | The default everywhere: site header, documents, slides, social profiles. On Limestone, Marble or any light, calm ground. |
| [`stoa-lockup-reversed.svg`](../logos/stoa-lockup-reversed.svg) | Primary, for dark grounds | On Night (`bg`, dark), Ink, or dark photography. A lighter Patina bubble and an Ink-light wordmark. |
| [`stoa-lockup-white.svg`](../logos/stoa-lockup-white.svg) | Primary, one color white | On a Patina fill, or on a dark photo where two colors would clash. |
| [`stoa-lockup-stacked.svg`](../logos/stoa-lockup-stacked.svg), `…-stacked-reversed.svg` | **Secondary**: the mark above the wordmark | Square and tall spaces: avatars with room for the name, title slides, stickers, merchandise. |
| [`stoa-mark.svg`](../logos/stoa-mark.svg), `…-reversed.svg` | **Secondary**: the mark alone | Where the name is already present or the space is small: the app header on phones, social avatars, watermarks. |
| [`stoa-mark-ink.svg`](../logos/stoa-mark-ink.svg), `stoa-mark-white.svg` | The mark in one color | Single-color printing, embossing, engraving, fax-quality reproduction. |
| [`stoa-wordmark.svg`](../logos/stoa-wordmark.svg) | The wordmark alone | Only where the mark already appears nearby, such as the footer of a page whose header has the mark. Never as the only identifier. |
| [`stoa-mark-16.svg`](../logos/stoa-mark-16.svg) | **Small-size mark**: the bubble, lintel, three straight columns and step on whole pixels | 16px only: tab icons, inline badges. |

The wordmark is "Stoa" in Spectral SemiBold, converted to outlines. It is never retyped: live text renders differently from browser to browser.

## Construction

![Construction, clear space and minimum sizes](images/logo-construction.png)

The mark is drawn on a 32-unit grid and spans 28 × 26 units.

- **Bubble:** 28 × 21, corners of radius 3.5.
- **Tail:** below the left of the bubble, 5 units wide and 5 deep: a vertical edge 5 units in from the bubble's left, and an edge at 45°.
- **Lintel:** 20 × 2.5, 4 units below the bubble's top.
- **Columns:** three, 6 units apart, 8.5 tall, 0.75 below the lintel. Each capital flares from 3.6 wide to 2.4 in one unit; the shaft widens to 2.8 at its foot.
- **Step:** 22 × 1.5, 0.75 below the columns and 3 above the bubble's bottom.

Everything but the bubble is a hole (`fill-rule="evenodd"`), not white paint.

In the lockup, the wordmark's cap height equals the bubble's height (21), and its baseline sits on the bubble's bottom, so the tail hangs below the line like a descender. The wordmark starts 6 units after the mark. The primary lockup is about 3.7 times as wide as it is tall, and the stacked lockup about 1.15 times as wide.

## Clear space

Keep **half the mark's height** clear on every side, measured from the outermost edges of the mark and the wordmark. No text, image edge, rule or other logo enters it. For a primary lockup 40px tall, that is 20px of clear space all round. The same rule applies to the mark alone and to the stacked lockup, where the measure is still the mark's height.

## Minimum sizes

| Asset | Digital | Print |
|---|---|---|
| Primary lockup | 20px tall | 6 mm tall |
| Stacked lockup | 40px tall | 12 mm tall |
| Mark | 20px tall | 6 mm tall |
| Mark below 20px | [`stoa-mark-16.svg`](../logos/stoa-mark-16.svg) at exactly 16px | Not used in print |

Below these sizes the columns run together and the wordmark's serifs break apart. Never use anything smaller than 16px, and never use the master mark between 16px and 20px.

## Color on grounds

| Ground | Logo |
|---|---|
| Limestone `#f3f4f2`, Marble `#ffffff`, any light neutral | Primary: a Patina mark and an Ink wordmark |
| Night `#121615`, Ink `#1d2422`, any dark neutral | Reversed |
| Patina `#2f7d6d` | White, one color |
| A photograph | White on a dark, calm area, or Ink on a light, calm area. Never across faces, text or busy detail. |
| One-ink print | Ink, or the print's single ink |

## Do's and don'ts

![Do's and don'ts](images/logo-dos-donts.png)

## Do

- Use the supplied files at their own proportions, scaled from a corner.
- Keep the clear space, even when space is tight. Choose a smaller size before a tighter margin.
- Choose the version by the ground: primary on light grounds, reversed on dark ones, white on Patina.
- Use the stacked lockup or the mark alone when the primary lockup would have to go below its minimum size.

## Don't

- **Stretch, squash or skew it.** Scale it proportionally only.
- **Rotate or tilt it.** The lintel is always level.
- **Recolor it.** Don't put the bubble in Rust or Ochre, use brand colors outside the approved schemes, or apply gradients.
- **Fill in the stoa** or paint it white. It is a hole; on any ground, the ground shows through it.
- **Add effects:** drop shadows, glows, outlines, bevels or transparency.
- **Place it on a clashing ground.** That includes the two-color logo on Patina, Rust or Ochre, the primary logo on a dark ground, and any version on a busy pattern or photo detail.
- **Rearrange it.** Don't put the wordmark before the mark, change the gap, or set the wordmark smaller or larger against the mark.
- **Retype the wordmark** in another font or weight, or change it to "STOA" or "stoa".
- **Redraw the mark.** Don't draw it as an outline, add a pediment, change the number of columns, flip the tail to the right, or change the bubble's corners.
- **Enlarge the 16px mark.** Its straight columns are only for 16px.

## Favicons

![Favicons](images/favicons.png)

Stoa's tab, home-screen and app icons, and the markup that loads them.

- `favicon.svg` is the primary favicon: the 16px mark in Patina, which switches to the lighter Patina in a dark browser.
- `favicon-32.png` and `favicon-16.png` are fallbacks for browsers that don't take SVG icons: a white mark on a Patina tile.
- `apple-touch-icon.png` (180) and `icon-512.png` are full-bleed Patina squares with the white mark in the central 56%. They are safe for iOS rounding and Android's maskable icons. Don't add corners or padding.
- Set `theme-color` to `bg`: `#f3f4f2` in light and `#121615` in dark.

```html
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/favicon-16.png" sizes="16x16" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#f3f4f2" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121615" media="(prefers-color-scheme: dark)">
```

In a web app manifest: `"icons": [{ "src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable" }]`.
