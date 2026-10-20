# Pop Star — FPV System

5.8GHz analog FPV on a 1/10 drift car. The video link is independent of the RC
control system — the Radiolink RC6GS V3 still controls the car on 2.4GHz; the FPV
video travels on its own 5.8GHz RF link to goggles or a monitor.

See `../harnesses/fpv-harness.wv` for the power wiring diagram.

---

## System overview

| Component | Chosen unit | Notes |
|---|---|---|
| **Camera + VTX (AIO)** | RunCam RC Cadet | Camera and 5.8GHz transmitter in one unit; single 2-pin power lead to ESC BEC. ~$30. |
| **Goggles** | Eachine EV800D | Box-style goggles with integrated 5.8GHz receiver. ~$55. Easy to hand to spectators at the track. |
| **5V regulator** | Pololu D24V5F5 | Required when BEC is set above 5V (e.g. 7.4V for servo). $5. Skip if BEC is set to 5V. |
| **Antenna** | Ships with RC Cadet | Linear dipole. Sufficient for indoor track distances. Replace with circular polarized if interference issues arise. |

**Total: ~$90** (including regulator)

**Analog vs digital:** Analog 5.8GHz has ~20ms latency and is adequate for the speeds and distances involved in indoor drift. Digital systems (DJI O3, HDZero) cost 3–4× more for image quality that doesn't benefit driving performance at these speeds. Analog recommended.

---

## Power

The XD10 Pro BEC outputs 5–7.4V adjustable at 5A continuous (set via item 1G). The RunCam RC Cadet draws ~400mA at 5V. The Pololu D24V5F5 regulator accepts 2.9–38V input, outputs regulated 5V at up to 500mA — well within budget.

**If BEC is set to exactly 5V:** wire BEC directly to camera, skip regulator.
**If BEC is set above 5V** (typical when running a 7.4V servo): insert the regulator.

An optional inline power switch on the VCC wire gives a hardware off capability independent of the VTX's pit mode. Recommended — a small slide switch adds ~$1 and eliminates any doubt about whether the transmitter is active.

---

## Disabling the VTX

Three ways to disable transmission at the track:

| Method | Notes |
|---|---|
| **Pit mode (0mW)** | Most VTX units have a 0mW setting via a button or solder pad. Zero RF output, still powered. RC Cadet: press the mode button to cycle to 0mW. |
| **Inline power switch** | Cut power to the entire FPV system. Recommended addition during install. |
| **Unplug the power lead** | One-connector disconnect if no switch installed. |

---

## Mounting — Phase 1 (24K lexan body)

The 24K TAF21000 is a closed coupe. Camera goes inside the body pointing forward through or above the windshield. A small 3D-printed bracket wedges between the body shell interior and the chassis; the camera lens protrudes just inside the windshield line. Antenna wire exits through a small hole drilled in the roof or A-pillar area, then routes along the body exterior.

**Bracket dimensions (print in PLA):**
- Position the camera at roughly driver's eye height inside the shell
- Keep the lens back from the windshield glass enough to avoid refraction (ideally touch the inner surface, or 1–2mm clearance)
- Use a thin foam pad or TPU bumper between the bracket and the chassis floor to reduce vibration

---

## Mounting — Phase 2 (custom cabriolet)

The open cabriolet body is purpose-made for FPV. Design the camera mount directly into the body structure in Blender:

- **Camera position:** driver's eye view, behind the A-pillars, looking forward through the windshield opening. At 1:10 scale the driver's eye is roughly 40–50mm above the chassis floor — a natural FPV angle that shows both front wheels and the track ahead.
- **Antenna routing:** the open top lets the antenna route straight up behind the roll cage. Design a small clip or guide into the roll cage top rail. The antenna sitting above the roll cage is both functional and visually appropriate.
- **Vibration isolation:** model a 2mm thick TPU pad between the camera mount surface and the inner frame floor. The pad absorbs drivetrain vibration that would otherwise blur the image.

Model the camera cavity at the correct lens cutout size (RC Cadet lens outer diameter: verify before modeling, typically 16–19mm for AIO units), with a 0.3mm clearance for SLS parts or 0.5mm for FDM.

---

## Integration with existing build

FPV uses **no RC radio channels** — it is a standalone video link. The RC6GS V3 / R7FG channel map in `build-decisions.md` is unaffected. Power comes entirely from the BEC via the regulator; no receiver port is needed.

The only wiring interaction is power: the BEC already powers the LED system (via Killerbody 48102 and the magnetic contact harness). The FPV system taps from the same BEC rail. Total additional BEC load: ~400mA at 5V. The XD10 Pro BEC is rated 5A continuous — this is not a concern.

| BEC consumers | Current draw |
|---|---|
| Servo (SX-12MGLP, 7.4V, no-load) | ~150mA |
| Killerbody 48102 + 4× LEDs | ~200mA |
| FPV AIO (RunCam RC Cadet) | ~400mA |
| Gyro (Yokomo DP-302 V4) | ~60mA |
| **Total** | **~810mA** |

Remaining headroom: ~4.2A. No concern.

---

## Track use note

RC Car World runs an indoor drift track. If they restrict 5.8GHz video transmitters (some tracks do due to multi-car interference), use pit mode or the inline switch to disable the VTX while not actively using FPV. The FPV system is fully independent from car control — disabling it does not affect driving.

---

## Sources

| Component | Product page |
|---|---|
| RunCam RC Cadet | [runcam.com](https://www.runcam.com/cameras/rc-cadet/) |
| Eachine EV800D | [eachine.com](https://www.eachine.com/products/ev800d) |
| Pololu D24V5F5 | [pololu.com](https://www.pololu.com/product/2843) |
