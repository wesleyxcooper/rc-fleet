# ASCII logo generator for Pop Star
#
# Font:  Dollie Script (free for personal use)
#        Designer: Måns Grebäck
#        Source: https://www.dafont.com/dollie-script.font
#        File:   assets/dollie-script.ttf
#
# Render the source PNG first (requires ImageMagick):
#   magick -size 700x150 xc:white \
#          -font assets/dollie-script.ttf \
#          -pointsize 110 -fill black \
#          -gravity Center -annotate 0 "Pop Star" \
#          assets/popstar-logo.png
#   magick assets/popstar-logo.png -trim +repage assets/popstar-logo-trim.png
#
# Then run this script (requires jp2a):
#   python3 assets/generate-ascii-logo.py
#
# The shooting star decorations (★ with diagonal tail) are derived from
# the Pop Star brand logo — a chrome shooting-star shape used as the
# car's identity mark.

import subprocess
from pathlib import Path

ASSETS = Path(__file__).parent

# Generate at width=80 (best readability for Dollie Script's flowing cursive)
result = subprocess.run(
    ["jp2a", "--width=80", "--chars= .,:;|*#@", "--invert", str(ASSETS / "popstar-logo-trim.png")],
    capture_output=True, text=True
)
lines = result.stdout.split('\n')
while lines and not lines[-1].strip():
    lines.pop()

# Pad every line to equal width
w = max(len(l) for l in lines)
lines = [l.ljust(w) for l in lines]

# Shooting star shape: star body + diagonal tail pointing toward the text
MARGIN = 4
total_w = w + MARGIN * 2

def pad(line, left=MARGIN):
    return ' ' * left + line

out = []

# Two rows above the art: shooting stars at left and right
row0 = ' ★' + ' ' * (total_w - 4) + '★ '
row1 = '  \\' + ' ' * (total_w - 5) + '/ '
out.append(row0)
out.append(row1)

# Art rows
for i, line in enumerate(lines):
    if i == 0:
        prefix = '   \\'   # tail continues
    else:
        prefix = '    '
    out.append(prefix + line)

# Small shooting star accent lower-right
pad_r = total_w - 3
out.append('')
out.append(' ' * pad_r + '★')
out.append(' ' * (pad_r - 1) + '/')
out.append(' ' * (pad_r - 2) + '/')

print('\n'.join(out))
