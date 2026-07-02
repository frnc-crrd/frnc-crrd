#!/usr/bin/env python3
"""Rotates the profile theme between the available palettes in themes/.
Reads the current theme from .theme, picks the next one, copies its assets
into assets/, patches the Mermaid diagram colors in README.md, and writes .theme.
"""
import os, shutil, re, pathlib

THEMES = ["amber", "violet"]
DIAGRAM = {
    "amber":  {"node": "#0F3A5F", "stroke": "#F5A623", "grp": "#0a2740", "grp_stroke": "#3a556e"},
    "violet": {"node": "#3A0CA3", "stroke": "#B57BED", "grp": "#22084d", "grp_stroke": "#4a2e6e"},
}

root = pathlib.Path(__file__).resolve().parent
state = root / ".theme"
current = state.read_text().strip() if state.exists() else THEMES[-1]
nxt = THEMES[(THEMES.index(current) + 1) % len(THEMES)] if current in THEMES else THEMES[0]

# 1) copy theme assets into assets/
src = root / "themes" / nxt
dst = root / "assets"
dst.mkdir(exist_ok=True)
for f in src.glob("*.svg"):
    shutil.copy(f, dst / f.name)

# 2) patch diagram colors in README
d = DIAGRAM[nxt]
readme = (root / "README.md").read_text()
readme = re.sub(r"classDef box fill:#[0-9a-fA-F]{6},stroke:#[0-9a-fA-F]{6}",
                f"classDef box fill:{d['node']},stroke:{d['stroke']}", readme)
readme = re.sub(r"classDef grp fill:#[0-9a-fA-F]{6},stroke:#[0-9a-fA-F]{6}",
                f"classDef grp fill:{d['grp']},stroke:{d['grp_stroke']}", readme)
(root / "README.md").write_text(readme)

# 3) save state
state.write_text(nxt + "\n")
print(f"Theme rotated: {current} -> {nxt}")
