# tokens.json -> tokens.css: custom properties for both themes, the font stacks and @font-face rules.
#   python3 source/tokens.py > tokens.css
import json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
t = json.loads((root / "tokens.json").read_text())
first, *rest = [th["id"] for th in t["color"]["themes"]]
val = lambda tok, theme: tok["value"] if isinstance(tok["value"], str) else tok["value"].get(theme, tok["value"][first])

out = ["/* Stoa — generated from tokens.json by source/tokens.py */"]
for f in t["type"]["fonts"]:
    out.append(f'@font-face {{ font-family: "{f["family"]}"; font-weight: {f["weight"]}; font-style: {f.get("style", "normal")}; font-display: swap; src: url(./{f["file"]}) format("woff2"); }}')
out.append(":root {")
out += [f'  --{tok["name"]}: {val(tok, first)};' for tok in t["color"]["tokens"]]
out += [f'  --{tok["name"]}: {tok["value"]};' for fam in ("spacing", "radius") for tok in t[fam]["tokens"]]
out += [f'  --font-{k}: {v};' for k, v in t["type"]["families"].items()]
out.append("}")
for theme in rest:
    block = [f'  --{tok["name"]}: {val(tok, theme)};' for tok in t["color"]["tokens"]] + ["  color-scheme: dark;"]
    out.append(f'@media (prefers-color-scheme: {theme}) {{ :root:not([data-theme="{first}"]) {{')
    out += ["  " + line for line in block]
    out.append("} }")
    out.append(f':root[data-theme="{theme}"] {{')
    out += block
    out.append("}")
print("\n".join(out))
