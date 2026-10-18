# ASCII logo generator for Pop Star
#
# Font:  Barbie Medium (free for personal use)
#        Source: https://fontmeme.com/fonts/barbie-medium-font/
#        File:   assets/barbie-medium.ttf
#
# Render the source PNG first (requires ImageMagick):
#   magick -background black -fill white -font assets/barbie-medium.ttf \
#          -pointsize 120 -gravity Center -size 900x200 \
#          label:"Pop Star" assets/popstar-logo.png
#   magick assets/popstar-logo.png -trim +repage assets/popstar-logo-trim.png
#
# Then run this script (requires jp2a):
#   python3 assets/generate-ascii-logo.py
#
# The shooting star decorations (★ with diagonal tail) are derived from
# the Pop Star brand logo — a chrome shooting-star shape used as the
# car's identity mark.

import subprocess

# Generate at a width that leaves room for margin decorations
result = subprocess.run(
    ["jp2a", "--width=64", "--chars= .,:;|*#@", "assets/popstar-logo-trim.png"],
    capture_output=True, text=True
)
lines = result.stdout.split('\n')
while lines and not lines[-1].strip():
    lines.pop()

# Pad every line to width
w = max(len(l) for l in lines)
lines = [l.ljust(w) for l in lines]

# Shooting star shape: star body + tail going lower-left
# Upper-left star at (0, 1), tail at (1, 0), (2, -1) → points toward text
# Upper-right star at (0, w+6), tail going lower-left down to text

# We'll build a canvas wider than the art, adding star decorations in the margin
MARGIN = 4
total_w = w + MARGIN * 2

def pad(line, left=MARGIN):
    return ' ' * left + line

out = []

# Two rows above the art: shooting stars at left and right
# Left star: tail points down-right ( \ )
# Right star: tail points down-left ( / )
row0 = ' ★' + ' ' * (total_w - 4) + '★ '
row1 = '  \\' + ' ' * (total_w - 5) + '/ '
out.append(row0)
out.append(row1)

# Art rows (the first 2 get continuation of the tails)
for i, line in enumerate(lines):
    prefix = pad('')
    if i == 0:
        prefix = '   \\'   # tail continues
    elif i == 1:
        prefix = '    '    # tail ends, art starts
    else:
        prefix = '    '
    out.append(prefix + line)

# A small shooting star to the lower-right as an accent
pad_r = total_w - 3
out.append('')
out.append(' ' * pad_r + '★')
out.append(' ' * (pad_r - 1) + '/')
out.append(' ' * (pad_r - 2) + '/')

print('\n'.join(out))
