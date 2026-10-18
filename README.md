# rc-fleet

Two-car RC fleet — both called **Pop Star**.

| Car | Platform | Purpose |
|---|---|---|
| [rc-popstar/](rc-popstar/) | HPI Stage-D10 Creator Edition (electric RWD drift) | Indoor competition + practice, RC Car World Cinnaminson NJ |
| — | HPI Nitro RS4 3 Drift (nitro 4WD, used) | Outdoor parking lot sessions |

**[Shopping list, build plan, and pricing →](shopping-list.md)**

---

## rc-popstar

Custom 1/10 RWD drift build on the Stage-D10 platform. BMW E36 cabriolet body (3D printed TPU, Lila Metallic, chrome/yellow graphics). Working lights via Killerbody 48102 LED control box with magnetic contact body interface.

Wiring is documented in [WireViz](https://github.com/wireviz/WireViz) format — plain text, git-diffable, renders SVG/HTML/BOM automatically.

| Harness | Diagram | Description |
|---|---|---|
| LED controller (D-Box3 Lite default) | [view](https://htmlpreview.github.io/?https://github.com/wesleyxcooper/rc-fleet/blob/main/rc-popstar/output/led-controller.html) | XD10 Pro BEC → KB48102 CH1/CH2 Y-cables → port outputs |
| Chassis harness | [view](https://htmlpreview.github.io/?https://github.com/wesleyxcooper/rc-fleet/blob/main/rc-popstar/output/chassis-harness.html) | KB48102 port outputs → 4× chassis-side magnetic contacts |
| Body harness | [view](https://htmlpreview.github.io/?https://github.com/wesleyxcooper/rc-fleet/blob/main/rc-popstar/output/body-harness.html) | Magnetic contacts → LED headlight + tail assemblies |
| Gyro variant: D-Box3 Pro | [view](https://htmlpreview.github.io/?https://github.com/wesleyxcooper/rc-fleet/blob/main/rc-popstar/output/gyro-dbox3-pro.html) | Adds PCA + AGS dials vs Lite |
| Gyro variant: Yokomo DP-302 V4 | [view](https://htmlpreview.github.io/?https://github.com/wesleyxcooper/rc-fleet/blob/main/rc-popstar/output/gyro-yokomo-dp302v4.html) | 4 modes, S.BUS dual gain via CH7 |

Build decision tree (gyro choice, LED delivery, BEC voltage vs resistor values): [`rc-popstar/docs/build-decisions.md`](rc-popstar/docs/build-decisions.md)

Magnetic contact interface design: [`rc-popstar/docs/magnetic-contact-design.md`](rc-popstar/docs/magnetic-contact-design.md)

To regenerate diagrams:

```bash
brew install graphviz
pip install -r rc-popstar/requirements.txt
wireviz rc-popstar/harnesses/*.wv -o rc-popstar/output/
```

---

## Related

- [e36-wiring](https://github.com/wesleyxcooper/e36-wiring) — full-size E36 Pop Star wiring (MaxxECU · ZF 8HP70 · Gauge.S cluster)
- [e36-build-docs](https://github.com/wesleyxcooper/e36-build-docs) — E36 build plan, BOM, walkthroughs
