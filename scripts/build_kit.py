"""Rebuild the two generated files in this repo.

    python3 scripts/build_kit.py

Reads:   tokens/tokens.json, guides/*.md, components/<Name>/README.md,
         assets/logos/README.md, assets/power-bi/ywca-knoxville-theme.json
Writes:  tokens/tokens.css       (the tokens as CSS variables)
         YWCA-DESIGN-KIT.md      (the whole kit in one file, for an AI assistant)

Run it after you change a token, a guide, or a component's README.
It needs Python 3 and nothing else.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8", newline="\n") as f:
        f.write(text.rstrip("\n") + "\n")


def without_title(markdown):
    """Drop a file's first-line '# Title' so it can sit under a heading of ours."""
    return re.sub(r"\A# [^\n]*\n+", "", markdown).strip()


def demote(markdown):
    """Push every heading down one level."""
    return re.sub(r"^(#+) ", lambda m: "#" + m.group(1) + " ", markdown, flags=re.M)


def table(rows, head):
    lines = ["| " + " | ".join(head) + " |", "| " + " | ".join("---" for _ in head) + " |"]
    lines += ["| " + " | ".join(str(cell).replace("|", "/") for cell in row) + " |" for row in rows]
    return "\n".join(lines)


tokens = json.loads(read("tokens/tokens.json"))
colors = {t["name"]: t for t in tokens["color"]["tokens"]}


def alias_of(value):
    """'{black}' means "the same as the black token". Returns 'black', or None."""
    m = re.fullmatch(r"\{([a-z0-9-]+)\}", value)
    return m.group(1) if m else None


def resolve(value):
    name = alias_of(value)
    return resolve(colors[name]["value"]) if name else value


# ------------------------------------------------------------- tokens.css
css = ["/* YWCA Knoxville design kit (unofficial draft). Made from tokens.json by scripts/build_kit.py. Do not edit by hand. */",
       ":root {", "  /* Color */"]
for t in tokens["color"]["tokens"]:
    name = alias_of(t["value"])
    css.append(f"  --{t['name']}: {'var(--' + name + ')' if name else t['value']};")
css.append("  /* Type families */")
for family, stack in tokens["type"]["families"].items():
    css.append(f"  --font-{family}: {stack};")
css.append("  /* Spacing */")
for t in tokens["spacing"]["tokens"]:
    css.append(f"  --{t['name']}: {t['value']};")
css.append("  /* Corners */")
for t in tokens["radius"]["tokens"]:
    css.append(f"  --{t['name']}: {t['value']};")
css += ["}", "", "/* Type styles. Display styles are set in capitals. */"]
for group in tokens["type"]["groups"]:
    for s in group["styles"]:
        rule = [f"font-family: var(--font-{group['family']})", f"font-size: {s['fontSize']}",
                f"line-height: {s['lineHeight']}", f"font-weight: {s['fontWeight']}"]
        if s.get("letterSpacing"):
            rule.append(f"letter-spacing: {s['letterSpacing']}")
        if group["family"] == "display" or s["name"] in ("nav", "label"):
            rule.append("text-transform: uppercase")
        css.append(f".t-{s['name']} {{ " + "; ".join(rule) + " }")
write("tokens/tokens.css", "\n".join(css))

# ----------------------------------------------------- YWCA-DESIGN-KIT.md
components = sorted(name for name in os.listdir(os.path.join(ROOT, "components"))
                    if os.path.exists(os.path.join(ROOT, "components", name, "README.md")))

kit = ["""# YWCA Knoxville design kit, in one file

This file holds the whole kit so an AI assistant can read it in one go. Give it to the assistant
at the start of a chat, then ask for what you need. People can read it too.

It is made from the other files in this repo by `scripts/build_kit.py`. Change those files, not this one.

## Instructions for the AI assistant reading this

You are helping staff and volunteers at YWCA Knoxville & the Tennessee Valley make things that
look and sound like YWCA: charts, reports, slides, flyers, web pages, and writing.

- Follow every rule in this file. When a request conflicts with a rule, say so in one sentence,
  then offer the closest thing that follows the rules.
- This kit is an unofficial working draft made by volunteers. YWCA has not reviewed it. Where
  this file and YWCA staff disagree, YWCA staff are right.
- Use only the colors, type styles, spacing, and components named here. Do not invent new ones.
- Never ask for, accept, or repeat a resident's name, birth date, address, room number, case
  note, or photo. If someone pastes one, tell them to remove it and carry on without it.
- Never show a count below five. Show "Fewer than 5" in its place.
- Write "YWCA", never "the YWCA". Write "women", "participants", or "residents".
- Never write a number, quote, or story about YWCA that you were not given. Ask for it.
- When you write code, use the token names (for example `var(--persimmon)`), not raw values.
- When you are not sure a rule applies, say what you assumed."""]

kit.append("## Brand rules\n\n" + demote(without_title(read("guides/brand-rules.md"))))

kit.append(
    "## Tokens\n\nThe same values are in `tokens/tokens.json` and, as CSS variables, in `tokens/tokens.css`.\n\n### Color\n\n"
    + table([(f"`{t['name']}`",
              resolve(t["value"]).upper() + (f" (same as `{alias_of(t['value'])}`)" if alias_of(t["value"]) else ""),
              t["usage"]) for t in tokens["color"]["tokens"]], ["Token", "Value", "Use"]))
kit.append("### Type families\n\n" + table([(f"`{k}`", v) for k, v in tokens["type"]["families"].items()],
                                           ["Family", "Font stack"]))
kit.append("### Type styles\n\n" + table(
    [(f"`{s['name']}`", g["family"], s["fontSize"], s["lineHeight"], s["fontWeight"], s["usage"])
     for g in tokens["type"]["groups"] for s in g["styles"]],
    ["Style", "Family", "Size", "Line height", "Weight", "Use"]))
kit.append("### Spacing\n\n" + table([(f"`{t['name']}`", t["value"], t["usage"]) for t in tokens["spacing"]["tokens"]],
                                     ["Token", "Value", "Use"]))
kit.append("### Corners\n\n" + table([(f"`{t['name']}`", t["value"], t["usage"]) for t in tokens["radius"]["tokens"]],
                                     ["Token", "Value", "Use"]))

parts = ["## Components\n\nEach one is plain HTML and CSS. The working markup is in `components/<Name>/preview.html`."]
for name in components:
    parts.append(f"### {name}\n\n" + without_title(read(f"components/{name}/README.md")))
kit.append("\n\n".join(parts))

kit.append("## Power BI\n\n" + demote(without_title(read("guides/power-bi.md"))))
kit.append("### The Power BI theme file\n\n```json\n" + read("assets/power-bi/ywca-knoxville-theme.json").strip() + "\n```")
kit.append("## Voice and writing\n\n" + demote(without_title(read("guides/voice-and-writing.md"))))
kit.append("## Print, slides, and other uses\n\n" + demote(without_title(read("guides/print-slides-and-other-uses.md"))))
kit.append("## Logos\n\n" + without_title(read("assets/logos/README.md")) + "\n\nThe files are in `assets/logos/`.")

write("YWCA-DESIGN-KIT.md", "\n\n".join(kit))
print(f"Wrote tokens/tokens.css and YWCA-DESIGN-KIT.md ({len(components)} components).")
