# Pop Star — Body Paint Guide

Target color: **BMW Individual Lila Metallic** (code 0490 / BASF FE86-403X).

The RC build uses a 3D-printed TPU body, so the painting process is exterior-facing
conventional spray — not the inside-out technique used on standard lexan bodies.

---

## Color Reference

| Field | Value | Source |
| :---- | :---- | :---- |
| BMW Individual code | **0490** | [carross.eu](https://www.carross.eu/en/paint-bmw-lila-met--490-fe86-403x-3082c) |
| BASF refinish formula | **FE86-403X** | [carross.eu](https://www.carross.eu/en/paint-bmw-lila-met--490-fe86-403x-3082c) |
| Autocolor cross-ref | MPE3B (pearl finish) | paintref.com |
| Finish type | Pearl metallic (2-coat: basecoat + clearcoat) | carross.eu |
| Production years | 1993–1997 | ral1.ru / carross.eu |
| Visual character | Warm magenta-hot-pink, leans distinctly pink rather than purple; metallic flake shifts by viewing angle | — |
| Measured hex | **#BC1C86** — measured with a color picker from a real Lila Metallic car photograph; represents one angle/lighting condition. The metallic flake will shift this value noticeably. | User-measured |

---

## Closest off-shelf paint matches to #BC1C86

Searched using [nickryden.github.io/paint-comparator](https://nickryden.github.io/paint-comparator/) (Euclidean RGB distance) and [cadetcraft.com](https://cadetcraft.com/data/paints/color/pink).

None of the miniature paint brands (Citadel, Vallejo, Army Painter, P3) carry a close match — their palettes don't extend to this saturation level. Scale75 Artist range is closest in the hobby category.

| Paint | Brand | Hex | Distance | Notes |
| :---- | :---- | :---- | :----: | :---- |
| **Magenta** | Scale75 Artist | `#C60A85` | ~20 | Closest overall; slightly higher red, lower green. Airbrush paint. |
| Carroburg Crimson | Citadel | `#A82A70` | 33 | Closest in Citadel/Vallejo/AP/P3 range; noticeably darker |
| Emperors Children | Citadel | `#B94278` | 41 | Lighter, more pink |
| Sunset Red | Vallejo Model | `#C22C5F` | 43 | Too red-pink |
| Murderous Magenta | P3 Formula | `#A81F5E` | 45 | Closest P3 option |

**For RC body work, none of the above are practical** — they're miniature-scale brush paints. For airbrush application on a 3D-printed body, see Options A–C below.

---

## Option A — Exact color, automotive basecoat (recommended)

Small-volume automotive basecoat in BMW 0490 is available from paint suppliers who
mix to code. This gives the exact color on a small body shell.

| Step | Material | Notes |
| :---- | :---- | :---- |
| 1 — Plastic primer | Tamiya Fine Surface Primer (gray), or automotive plastic adhesion promoter | Required for paint adhesion on TPU. Two light coats, let cure 24 h. |
| 2 — Basecoat | BMW 0490 / FE86-403X basecoat, from a BMW-code supplier | 123lack.de sells basecoat in 100 mL cans ([123lack.de](https://www.123lack.de/basislack-bmw-490-lila-metallic-autolack-2-schicht)). Two thin passes, 10-15 min between. |
| 3 — Clearcoat | Automotive 2K clearcoat, or Tamiya TS-13 Clear | Required — basecoat is not self-sealing. Two coats. |

**Amazon-available source:** "Lila Metallic 490 Automotive Paint – OEM Color Match – For BMW Vehicles" by DipYourCar, [Amazon B0GMRL64MB](https://www.amazon.com/dp/B0GMRL64MB), $21.49 for 2 fl oz. Same workflow as above — needs reducer and clearcoat, requires a spray gun or airbrush; not a rattle can. 2 fl oz is the right quantity for an RC body shell. DipYourCar is primarily a Plasti-Dip brand; their metallic color accuracy is not independently verified, but for RC scale it does not need to be exact.

**Note on TPU compatibility:** Automotive basecoat is flexible when cured and bonds
well to primed TPU. Apply in thin coats; thick single coats can crack under flex.
Do not skip the adhesion primer step.

---

## Option B — Off-shelf Tamiya polycarbonate spray (for lexan; closest to color)

If switching to an APlastics E36 lexan body instead of the 3D-printed version,
use Tamiya PS series paints (designed for polycarbonate, applied inside-out).

| Product | Code | Character | Match quality |
| :---- | :---- | :---- | :---- |
| **Tamiya Metallic Purple** | PS-18 | Purple metallic, leans blue-purple | Moderate — shifts more blue than BMW Lila Metallic |
| **Tamiya Purple Anodized Aluminum** | PS-51 | Strong purple metallic with aluminum effect; add black backing layer for richer depth | Better — more saturated, but still bluer than the BMW color |
| **Tamiya Iridescent Purple/Green** | PS-46 | Shifts between purple and green at angle | Not a match — iridescent, not metallic purple |

**Tip for PS-51:** spray one coat of PS-51, then back it with a coat of PS-2 (Red)
before the black backing layer. The red tint pulls the purple slightly toward magenta
for a closer match to Lila Metallic's pink-purple character.

Source: [Tamiya PS-51 product page](https://tamiya.com/english/products/86051/index.html)
Source: [Tamiya PS-18 at Excel RC](https://www.excelrc.com/products/tamiya-polycarbonate-paint-ps-18-metallic-purple)

---

## Option C — Mixing approach (airbrushed 3D-printed body)

For the closest possible match on the 3D-printed body using an airbrush:

1. **Prime:** gray automotive plastic primer
2. **Metallic base:** Alclad II Polished Aluminum or Alclad II Chrome (thin, smooth coat)
3. **Candy color:** Alclad II Candy Magenta + Candy Purple, mixed approximately 50/50 — adjust by eye against BMW reference photos
4. **Clearcoat:** Alclad II Aqua Gloss or automotive 2K clear

The Alclad candy-over-chrome method reproduces the depth and angle-shift behavior of a
metallic pearl paint more faithfully than single-pass spray cans.

---

## Graphics

**"Pop Star" vinyl lettering** in Dollie Script font. Font file: [`../assets/dollie-script.ttf`](../assets/dollie-script.ttf) — by Måns Grebäck, free for personal use ([dafont.com](https://www.dafont.com/dollie-script.font)).

Placement options:
- Rear 3/4 of body shell (below window line)
- Rear windshield panel (script across lower glass area)

Size for the rear window: roughly 45mm × 18mm lettering at ~12mm cap height. Reads well from a meter.

Print white or chrome on the Lila Metallic base. Order from a local sign shop or a custom vinyl service (Sticker Mule, Unstoppable Graphics). Specify matte finish to avoid glare under track lighting.

---

## Phase 1 lexan body painting (24K TAF21000)

Standard RC lexan/polycarbonate bodies are painted **from the inside**. The exterior surface stays clear and untouched. This is the opposite of conventional model painting.

**Workflow:**
1. Mask window edges on the exterior with vinyl masking tape or liquid mask.
2. Spray the interior surface — color coats first, then a white or silver backing layer for opacity.
3. The paint shows through the clear exterior, giving a glassy depth.
4. Trim lines are defined by where you masked.

All Tamiya PS, Parma, and similar lexan spray lines are formulated for this — they flex with the body instead of cracking. Regular spray paint will crack and peel off lexan.

**Tamiya PS colors for the Lila Metallic look on lexan:**

| Product | Code | Character | Match quality |
|---|---|---|---|
| **Tamiya Metallic Purple** | PS-18 | Purple metallic, leans blue-purple | Moderate — shifts more blue than BMW Lila Metallic |
| **Tamiya Purple Anodized Aluminum** | PS-51 | Strong purple metallic with aluminum effect | Better — more saturated, but still bluer than the BMW color |
| **Tamiya Iridescent Purple/Green** | PS-46 | Shifts between purple and green at angle | Not a match — iridescent, not metallic purple |

**Tip for PS-51:** spray one coat of PS-51, then back it with a coat of PS-2 (Red) before the black backing layer. The red tint pulls the purple slightly toward magenta for a closer match to Lila Metallic's pink-purple character.

**Available at RC Car World** (local, full range stocked): PS series $8–12/can.

Source: [Tamiya PS-51](https://tamiya.com/english/products/86051/index.html) · [Tamiya PS-18 at Excel RC](https://www.excelrc.com/products/tamiya-polycarbonate-paint-ps-18-metallic-purple)
