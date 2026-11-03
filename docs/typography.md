# Typography

Three families, each with one job. All three are under the SIL Open Font License, and ship as WOFF2 in `fonts/` to be served from Stoa's own origin.

| Family | Role | Weights | Fallback stack |
|---|---|---|---|
| **Spectral** (Production Type) | Headers and graphics: what you read first | 600 SemiBold; 500 Medium for 40px and up | `"Spectral", Georgia, "Times New Roman", serif` |
| **Public Sans** (USWDS) | Body copy, controls, captions | 400 Regular, 600 SemiBold (one variable file) | `"Public Sans", system-ui, -apple-system, "Segoe UI", Helvetica, Arial, sans-serif` |
| **JetBrains Mono** | Data: account IDs, CIDs, chain paths | 400 Regular | `"JetBrains Mono", ui-monospace, Menlo, Consolas, monospace` |

Spectral is a screen-first serif with a scholarly, literary voice, which fits a forum named for a place of public argument. Public Sans is neutral and highly legible, built for public services. JetBrains Mono keeps similar characters apart (0 and O, 1 and l), which matters when someone checks an address character by character.

## Roles

| Role | Style | Family and weight | Size / line height | Case |
|---|---|---|---|---|
| Page header | `page-title` | Spectral 600 | 26 / 1.2 | Sentence |
| Dialog header | `dialog-title` | Spectral 600 | 20 / 1.25 | Sentence |
| Post title | `post-title` | Spectral 600 | 19 / 1.3 (17.5 on phones) | As the author wrote it |
| Panel header | `panel-title` | Spectral 600 | 18 / 1.3 | Sentence |
| Section header | `section` | Spectral 600 | 15 / 1.4 | Sentence |
| Figures | `stat` | Spectral 600, tabular | 20 / 1.2 | — |
| Body copy | `body` | Public Sans 400 | 15 / 1.5 | Sentence |
| Controls | `control`, `control-strong` | Public Sans 400; 600 on primary | 14 / 22px | Sentence |
| Secondary copy | `small` | Public Sans 400 | 13.5 / 1.5 | Sentence |
| Meta lines, labels | `meta` | Public Sans 400, `muted` | 12.5 / 1.5 | Sentence |
| Captions | `caption` | Public Sans 400, `muted` | 12 / 1.4 | Sentence |
| Eyebrow labels | `eyebrow` | Public Sans 600, `muted`, +0.08em | 11 / 1.4 | UPPERCASE |
| Data | `data` | JetBrains Mono 400 | 12 / 1.5 | As written |
| Graphic headline | `graphic-headline` | Spectral 500, −0.01em | 56 / 1.05 | Sentence |
| Graphic subhead | `graphic-subhead` | Spectral 600 | 24 / 1.3 | Sentence |
| Graphic body | `graphic-body` | Public Sans 400 | 18 / 1.45 | Sentence |

Graphics (social cards, slides, posters) scale the three graphic styles together. Keep the headline between 2 and 3.5 times the body size, and give the headline one short line.

## Case

- **Sentence case** for everything: headers, buttons, menus, tabs, labels, graphics. Examples: "Continue with Selfhold", "Your communities", "Sign in".
- **Title Case** is never used, except within proper names: Stoa, Lattice, Selfhold, Moniker, Follows.
- **UPPERCASE** appears only in eyebrow labels, always with 0.08em tracking. Never set a whole header or button in capitals.
- **Lowercase** for community names (`s/bitcoin`) and handles (`@ada`), even at the start of a sentence.
- The name is always "Stoa": never "STOA", "stoa" or "StoA", in text or in graphics.

## Setting

- Keep body lines near 65 characters, with a 15px size and 1.5 line height.
- Headers wrap with `text-wrap: balance`. Long words and addresses break with `overflow-wrap: anywhere` rather than overflowing.
- Use tabular numerals (`font-variant-numeric: tabular-nums`) for vote counts, figures and anything set in columns.
- Use only the two weights, 400 and 600. Don't use bold (700), light weights or italics in the interface. Spectral 500 appears only in graphics at 40px and up.
- Set links in `ink` with a Patina underline, never as Patina text at body sizes. Don't set any text in Rust or Ochre without a word that also carries the meaning.
- The smallest text is 12px, except the 11px eyebrow, which is uppercase and bold enough to hold.

## Web-safe fallbacks

Each stack falls back to a face that keeps the role's shape: Georgia for Spectral (a sturdy screen serif), the system UI face for Public Sans, and the platform's monospace for JetBrains Mono. All the fonts load with `font-display: swap`, so text shows at once in the fallback and then switches. Never load the brand fonts from a third-party host such as Google Fonts in Stoa itself: serving them from Stoa's origin is part of the privacy promise.

```css
@font-face { font-family: "Spectral"; font-weight: 600; font-display: swap; src: url(../fonts/spectral-600.woff2) format("woff2"); }
@font-face { font-family: "Spectral"; font-weight: 500; font-display: swap; src: url(../fonts/spectral-500.woff2) format("woff2"); }
@font-face { font-family: "Public Sans"; font-weight: 400 600; font-display: swap; src: url(../fonts/public-sans.woff2) format("woff2"); }
@font-face { font-family: "JetBrains Mono"; font-weight: 400; font-display: swap; src: url(../fonts/jetbrains-mono-400.woff2) format("woff2"); }
```
