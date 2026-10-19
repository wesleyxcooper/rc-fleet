# ASCII logo generator for Pop Star
#
# Source image: assets/popstar-logo-official.png
#   Official Pop Star logo — "Pop ★ Star" with shooting stars designed by Wesley.
#   Dollie Script font by Mans Grebaek (dafont.com/dollie-script.font).
#
# Pipeline:
#   1. Flatten the logo onto a white background (it may have transparency)
#   2. Convert to grayscale and threshold to clean black/white
#   3. Trim white padding
#   4. Run jp2a with --invert so letter shapes appear as open space in a
#      dense character field — reproduces all three stars and the full
#      letterform layout from the actual logo design
#
# Requires: ImageMagick (magick), jp2a, Pillow
#   brew install imagemagick jp2a
#   pip install pillow
#
# Usage:
#   python3 assets/generate-ascii-logo.py

import subprocess
from pathlib import Path

ASSETS  = Path(__file__).parent
SRC     = ASSETS / "popstar-logo-official.png"
BW      = ASSETS / "popstar-logo-trim.png"    # intermediate BW used by jp2a

# --- convert official logo to clean black-on-white ---
subprocess.run([
    "magick", str(SRC),
    "-background", "white", "-flatten", "-alpha", "off",
    "-colorspace", "Gray",
    "-threshold", "50%",
    "-trim", "+repage",
    str(BW),
], check=True)

# --- ascii render ---
# --invert: logo ink (black after threshold) renders as space;
#           white background renders as dense characters.
# This "hollow" style traces the actual logo layout including all three stars.
result = subprocess.run(
    ["jp2a", "--width=150", "--chars= .,:;|*#@", "--invert", str(BW)],
    capture_output=True, text=True, check=True
)

lines = result.stdout.split("\n")
while lines and not lines[0].strip():
    lines.pop(0)
while lines and not lines[-1].strip():
    lines.pop()

print("\n".join(lines))
