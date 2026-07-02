#!/usr/bin/env python3
"""Rotate the profile theme by REWRITING the image paths in README.md.
No file copying, no assets/ folder: the README points straight to
themes/<active>/... . Because switching palettes changes the URL
(themes/amber/... -> themes/violet/...), GitHub serves the new image
immediately with no camo-cache lag. The active theme is whatever path
the README currently uses; we flip it to the next one each run.
"""
import sys, re, pathlib

THEMES = ["amber", "violet"]
DIAGRAM = {
    "amber":  {"node": "#0F3A5F", "stroke": "#F5A623", "grp": "#0a2740", "grp_stroke": "#3a556e"},
    "violet": {"node": "#3A0CA3", "stroke": "#B57BED", "grp": "#22084d", "grp_stroke": "#4a2e6e"},
}

root = pathlib.Path(__file__).resolve().parent
readme_path = root / "README.md"
readme = readme_path.read_text()

# Detect current theme from the paths in the README
current = next((t for t in THEMES if f"themes/{t}/" in readme), None)
if current is None:
    sys.exit("::error::No 'themes/<name>/' image paths found in README.md. "
             "Make sure the README points to themes/amber/ or themes/violet/.")
nxt = THEMES[(THEMES.index(current) + 1) % len(THEMES)]

# Sanity: the next theme folder must exist with svgs
src = root / "themes" / nxt
if not src.is_dir() or not list(src.glob("*.svg")):
    sys.exit(f"::error::Theme '{nxt}' missing or empty at {src}.")

# 1) flip every image path
readme = readme.replace(f"themes/{current}/", f"themes/{nxt}/")

# 2) flip diagram colors to match
d = DIAGRAM[nxt]
readme = re.sub(r"classDef box fill:#[0-9a-fA-F]{6},stroke:#[0-9a-fA-F]{6}",
                f"classDef box fill:{d['node']},stroke:{d['stroke']}", readme)
readme = re.sub(r"classDef grp fill:#[0-9a-fA-F]{6},stroke:#[0-9a-fA-F]{6}",
                f"classDef grp fill:{d['grp']},stroke:{d['grp_stroke']}", readme)

readme_path.write_text(readme)
print(f"Theme rotated in README: {current} -> {nxt}")