# Magnetic Contact Interface Design

Body-chassis electrical interface for the Pop Star RC D10 light system.
Implements Option 3: OEM body post magnets as GND return, new satellite magnets
as LED+ hot conductors.

---

## Concept

Each body post corner has two magnets:
- **OEM body post magnet** — already present on the D10, already at chassis GND.
  No modification. Provides mechanical attachment AND GND return path.
- **Satellite disc magnet** — new, added adjacent to the body post.
  Wired to LED+ on the chassis side, wired to LED anode on the body side.
  Provides the hot (+) conductor.

When the body shell is placed on the chassis, both magnets at each corner
attract simultaneously: mechanical attachment and electrical circuit closure are
the same motion. Lights come on as the body seats. No separate plug step.

This is structurally identical to a real vehicle headlight bulb seated in its
socket: the socket provides both mechanical retention and electrical contact.

---

## Magnet Specifications

### Satellite magnets (new — 4 required, 8 total: 4 chassis-side, 4 body-side)

| Parameter | Value |
|---|---|
| Grade | N52 NdFeB |
| Geometry | Disc, 6mm diameter × 3mm thick |
| Plating | Nickel (corrosion resistant, electrically conductive) |
| Pull force (6mm N52 disc) | ~1.1 kg (9mm pair face-to-face) |
| Bulk resistivity | ~1.6 µΩ·m |
| Estimated contact resistance | < 50 mΩ at 6mm contact area |
| Voltage drop at 20 mA | < 1 mV (negligible) |

Suggested source: K&J Magnetics D62 or equivalent. Amazon or supermagnete.com.
Buy 10 to have extras; price is negligible ($0.30–0.50 each in packs).

### OEM D10 body post magnets (existing — no purchase required)

Verify dimensions from D10 assembly guide. Expected: N52 disc, ~12–15mm OD.
These are already at chassis GND — no wiring change.

---

## Polarity Convention

Magnets must attract across the body-chassis gap. Polarity must be consistent
at each corner so the body only seats one way (which it already enforces
mechanically via the body post locations).

| Side | Face direction | Satellite pole |
|---|---|---|
| Chassis | Up (toward body) | **South** |
| Body | Down (toward chassis) | **North** |

Mark each satellite magnet with a paint pen or Sharpie dot on the South face
before installing — once epoxied in, you cannot easily determine polarity.

OEM body post magnets: determine their polarity before installing satellite
magnets nearby. Use a compass or a known-polarity magnet to check. The body
post magnet's chassis-facing pole determines what pole the body-side body post
magnet must be (opposite to attract).

---

## Chassis-Side Installation

### Satellite magnet bracket

3D print in PETG (rigid, chemical resistant). One bracket per body post corner.

Bracket function:
- Positions satellite magnet 15–20mm from body post center (far enough to clear
  the body post magnet field, close enough to keep body harness short)
- Provides electrical isolation between satellite magnet and chassis rail
  (PETG is non-conductive)
- Attaches to existing body post boss on chassis without modification (friction
  fit or small M2 screw into printed boss)

Magnet seat: 6.1mm dia × 3.1mm deep pocket (0.1mm press-fit clearance).
Press magnet in with flat-nosed pliers; add thin CA glue bead around perimeter.

Wire routing from satellite magnet: 26 AWG single conductor exits the bracket
through a channel, routes under chassis rails to LED controller header. Use
adhesive wire guides (Panduit style or 3D-printed clips).

### GND return

No additional wiring on chassis side for GND. The OEM body post magnet is
already at chassis GND (the D10's chassis is a conductive metal/composite
structure tied to the ESC/battery negative). The body post magnet face that
contacts the body-side body post magnet closes the GND circuit when the body
seats.

If chassis-side GND needs to be verified with a multimeter: probe between
the OEM body post magnet face and the battery negative — should read < 0.5Ω.

---

## Body-Side Installation

### Satellite magnet pocket

Model directly into the Blender body design. Pocket geometry:
- 6.1mm dia × 3.1mm deep (same press-fit spec)
- Located in the body underside at the position matching the chassis bracket
- Surrounded by PETG/TPU body wall — electrically isolated

### Body post magnet receiver seat

The OEM D10 body post slides into a receiver seat molded into the body
underside. This receiver seat keeps the body-side body post magnet in contact
with the chassis post magnet.

Add a small conductive pad (copper foil or thin brass sheet, ~10mm × 10mm) to
the inner face of the body post receiver seat. Solder the GND return wire from
the LED cathode to this pad. When the body post seats, the pad contacts the
chassis-side body post magnet → GND circuit closes.

Alternatively, embed a matching body-side N52 disc magnet into the body post
receiver seat (larger diameter, same as chassis OEM post magnet) and solder
the wire to it directly. This provides stronger attraction AND reliable contact.

---

## Electrical Summary

| Path | Conductor | Current | Notes |
|---|---|---|---|
| LED+ (chassis → body) | 6mm N52 satellite magnet pair | ≤ 20 mA per LED | Negligible resistance |
| GND return (body → chassis) | OEM body post magnet + contact pad | ≤ 20 mA per LED | Negligible resistance |
| Total per corner | — | ≤ 20 mA | One LED per corner |
| Total system | — | ≤ 80 mA | 4 LEDs simultaneously |

BEC supply from R7FG receiver: 5V / 3A. At 80 mA LED draw + ~50 mA receiver
overhead, total BEC load is well under 200 mA. No thermal concern.

---

## Failure Modes

| Failure | Symptom | Fix |
|---|---|---|
| Satellite magnet wrong polarity | Body repels at that corner | Flip satellite magnet, re-press and re-epoxy |
| Satellite magnet not wired (open) | That corner LED never illuminates | Check continuity from header to satellite magnet face |
| GND contact pad not touching post magnet | LED+ present but no return path → LED off | Add thicker copper pad or reposition body post receiver seat |
| LED+ shorted to GND inside body | LED always on regardless of controller state | Check that satellite and body post magnets are not bridged by conductive body paint |
| Two corners cross-connected | Incorrect channel lighting | Verify wire color discipline: RD = LED+, BK = GND throughout |

---

## Build Sequence

1. Print chassis-side satellite magnet brackets (PETG)
2. Verify OEM body post magnet polarity at all 4 corners
3. Determine correct satellite magnet polarity per above convention
4. Mark satellite magnets before pressing into brackets
5. Route chassis harness (chassis-harness.wv), secure with adhesive guides
6. Build and bench-test chassis harness with a spare LED before body shell is printed
7. Print body shell with satellite magnet pockets and LED housing channels modeled in
8. Press body-side satellite magnets into pockets; epoxy
9. Install body-side GND contact pads at body post receiver seats
10. Run body harness wires (body-harness.wv), splice resistors inline
11. Install 5mm LEDs in headlight and tail lamp housings; press in lens domes
12. Bench test body harness independently (touch chassis-side satellite magnet face to
    body-side satellite magnet to simulate contact; LEDs should illuminate)
13. Mount body shell → verify all 4 LEDs illuminate; check polarity/brightness
