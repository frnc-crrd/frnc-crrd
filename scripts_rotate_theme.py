#!/usr/bin/env python3
"""Rotate the profile theme between the palettes in themes/.
Single source of truth = .theme. Each run advances to the NEXT theme and
applies BOTH its assets and its diagram colors atomically, so the banner,
buttons and Mermaid diagram are ALWAYS in sync.
"""
import sys, shutil, re, pathlib

THEMES = ["amber", "violet"]
DIAGRAM = {
    "amber":  {"node": "#0F3A5F", "stroke": "#F5A623", "grp": "#0a2740", "grp_stroke": "#3a556e"},
    "violet": {"node": "#3A0CA3", "stroke": "#B57BED", "grp": "#22084d", "grp_stroke": "#4a2e6e"},
}

root = pathlib.Path(__file__).resolve().parent
state = root / ".theme"
current = state.read_text().strip() if state.exists() else THEMES[-1]
nxt = THEMES[(THEMES.index(current) + 1) % len(THEMES)] if current in THEMES else THEMES[0]

src = root / "themes" / nxt
dst = root / "assets"
if not src.is_dir() or not list(src.glob("*.svg")):
    sys.exit(f"::error::Theme '{nxt}' missing or empty at {src}. Upload themes/ fully.")

# 1) assets
n = 0
for f in src.glob("*.svg"):
    shutil.copy(f, dst / f.name); n += 1

# 2) diagram (always matches nxt)
d = DIAGRAM[nxt]
readme = (root / "README.md").read_text()
readme = re.sub(r"classDef box fill:#[0-9a-fA-F]{6},stroke:#[0-9a-fA-F]{6}",
                f"classDef box fill:{d['node']},stroke:{d['stroke']}", readme)
readme = re.sub(r"classDef grp fill:#[0-9a-fA-F]{6},stroke:#[0-9a-fA-F]{6}",
                f"classDef grp fill:{d['grp']},stroke:{d['grp_stroke']}", readme)
(root / "README.md").write_text(readme)

# 3) state
state.write_text(nxt + "\n")
print(f"Theme rotated: {current} -> {nxt}  ({n} assets + diagram in sync)")
