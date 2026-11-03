# Color

Stoa's colors come from its namesake: pale limestone and marble, dark ink, and bronze weathered to patina. Rust and ochre are earth pigments, used only to signal a state. Each color is a token with a light and a dark value; build with the token name, not the hex.

## Primary

| Name | Token | HEX | RGB | CMYK | Role |
|---|---|---|---|---|---|
| Patina | `accent` | `#2F7D6D` | 47, 125, 109 | 62, 0, 13, 51 | The brand's color: the logo's roof, primary actions, links, focus |
| Ink | `ink` | `#1D2422` | 29, 36, 34 | 19, 0, 6, 86 | All text, the logo's columns and wordmark |

## Secondary

| Name | Token | HEX | RGB | CMYK | Role |
|---|---|---|---|---|---|
| Limestone | `bg` | `#F3F4F2` | 243, 244, 242 | 0, 0, 1, 4 | Page ground |
| Marble | `surface` | `#FFFFFF` | 255, 255, 255 | 0, 0, 0, 0 | Cards, panels, dialogs |
| Slate | `muted` | `#5D6764` | 93, 103, 100 | 10, 0, 3, 60 | Secondary text |
| Hairline | `line` | `#DDE1DE` | 221, 225, 222 | 2, 0, 1, 12 | Borders and dividers |
| Patina tint | `accent-soft` | `#E2EFEB` | 226, 239, 235 | 5, 0, 2, 6 | Selected and upvoted grounds |

## Accent

| Name | Token | HEX | RGB | CMYK | Role |
|---|---|---|---|---|---|
| Rust | `down` | `#9A5B45` | 154, 91, 69 | 0, 41, 55, 40 | Downvotes, collapsed items, errors |
| Rust tint | `down-soft` | `#F5E6E0` | 245, 230, 224 | 0, 6, 9, 4 | Downvoted grounds |
| Ochre | `warn` | `#7A5F12` | 122, 95, 18 | 0, 22, 85, 52 | Notices that need attention |
| Ochre tint | `warn-soft` | `#F6EFD9` | 246, 239, 217 | 0, 3, 12, 4 | Notice grounds |

## Dark theme

The dark theme is its own palette, not an inversion of the light one. Patina is lighter so that it holds contrast on Night, and text on a Patina fill turns dark.

| Name | Token | HEX | RGB | CMYK |
|---|---|---|---|---|
| Patina | `accent` | `#5FB8A3` | 95, 184, 163 | 48, 0, 11, 28 |
| Ink | `ink` | `#E5EBE8` | 229, 235, 232 | 3, 0, 1, 8 |
| Night | `bg` | `#121615` | 18, 22, 21 | 18, 0, 5, 91 |
| Night raised | `surface` | `#1A201E` | 26, 32, 30 | 19, 0, 6, 87 |
| Slate | `muted` | `#9AA5A1` | 154, 165, 161 | 7, 0, 2, 35 |
| Hairline | `line` | `#2B3331` | 43, 51, 49 | 16, 0, 4, 80 |
| Patina tint | `accent-soft` | `#1F3530` | 31, 53, 48 | 42, 0, 9, 79 |
| On Patina | `on-accent` | `#0B1714` | 11, 23, 20 | 52, 0, 13, 91 |
| Rust | `down` | `#D08B72` | 208, 139, 114 | 0, 33, 45, 18 |
| Rust tint | `down-soft` | `#33231D` | 51, 35, 29 | 0, 31, 43, 80 |
| Ochre | `warn` | `#D9B65C` | 217, 182, 92 | 0, 16, 58, 15 |
| Ochre tint | `warn-soft` | `#2E2918` | 46, 41, 24 | 0, 11, 48, 82 |

The CMYK values are direct conversions from sRGB, with no ICC profile. For print, convert in your layout tool with the printer's profile (for example, Coated FOGRA39 or GRACoL 2013) and proof Patina before a run. A muted teal-green shifts more than most colors on uncoated stock.

## Proportion

Grounds and Ink cover almost every screen. Patina stays under a tenth of any view: one primary button, the links, the selected item. Rust and Ochre appear only where something is down-voted, collapsed or needs attention. A page with no state to show has none.

## Contrast and accessibility

The targets are WCAG 2.2 AA:
- 4.5:1 for text;
- 3:1 for text 24px and up, or 600 weight at 19px and up;
- 3:1 for focus rings, icons and control borders that carry meaning.

| Pair | Light | Dark | Use |
|---|---|---|---|
| `ink` on `bg` | 14.3 | 15.1 | Body text: passes everywhere |
| `ink` on `surface` | 15.8 | 13.7 | Body text on cards |
| `muted` on `bg` | 5.3 | 7.2 | Meta lines, captions |
| `muted` on `surface` | 5.9 | 6.5 | Meta lines on cards |
| `accent` on `surface` | 4.9 | 7.0 | Links and patina text on cards |
| `accent` on `bg` | **4.45** | 7.7 | Fails AA for small text in light by 0.05. Set small links in `ink` with a Patina underline, and use Patina text only at 600 weight, 19px and up. |
| `on-accent` on `accent` | 4.9 | 7.7 | Primary button labels |
| `accent` on `accent-soft` | **4.16** | 5.5 | Fails AA for small text in light. Use `ink` for small text on the tint. |
| `down` on `surface` | 5.3 | 6.0 | Error text |
| `down` on `down-soft` | **4.37** | 5.5 | Fails AA for small text in light. Only the bold vote count goes here. |
| `warn` on `warn-soft` | 5.3 | 7.5 | Notice text |
| White on Patina | 4.9 | — | The white logo and the app icon |
| `line` on `surface` | 1.3 | 1.3 | Decorative only, never the only sign of a control |

Rules:
- **Links:** `ink` text with a 1px Patina underline, offset 3px, turning Patina on hover. The text holds 14:1 on any ground, and the underline keeps the brand color.
- **Focus:** a solid 2px `accent` outline, offset 2px. It is at least 3:1 on every ground in both themes (4.45 on Limestone, 4.9 on Marble, 7.0 or more in dark).
- **Color plus a cue:** never let color be the only signal. An upvote is Patina and an up arrow; a downvote is Rust and a down arrow; a collapsed post says "Collapsed". Patina and Rust are almost the same lightness (1.08:1), so the arrow and the word are what tell them apart.
- **Grounds for the logo:** the two-color logo needs a ground on which Patina reaches 3:1. That is true of Limestone, Marble and white (4.45–4.9); on Night, use the reversed logo (7.7).
- **Respect the reader's theme.** Ship both themes, choose by `prefers-color-scheme`, and let an explicit setting override it.
