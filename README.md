# ZMK Firmware for Graph Theory based keyboards

A ZMK module holding a collection of keyboard firmware for my keyboard PCB designs.
These use Graph Theory based sparse scanning matrices to avoid ghosting, rather than diodes.
They have simple minimal Qwerty layouts including ZKM Studio support to cover basic usage:

* [Gamma Omega TC36K](boards/shields/tc36k), a Graph Theory based diode-free keyboard with
  26 GPIO pins for 36 keys and 6-key roll-over using a partial Tutte-Coxeter Graph.
* [Gamma Omega Hesse](boards/shields/hesse), a Graph Theory based diode-free Bluetooth
  keyboard with 21 GPIO pins for 36 keys and 4-key roll-over using the Hesse Configuration
  Incidence Graph.
* [Forager Acid](boards/shields/acid), a Graph Theory based diode-free Bluetooth split
  keyboard with 13 GPIO pins for 17 (or 18) keys and 4-key roll-over per half using a
  partial Heawood Graph.

See also my [QMK keyboard firmware](https://github.com/peterjc/qmk_userspace).

## Usage

If you had built one of my keyboard PCB designs you can download the [latest build
of firmware for these keyboards](https://github.com/peterjc/zmk-keyboard-graph-theory/releases/tag/latest),
using a default Qwerty layout with ZMK Studio enabled as a starting point.

If you then wanted to customise the firmware, you would probably want to clone the
[Unified ZMK Config Template](https://github.com/zmkfirmware/unified-zmk-config-template),
and include a reference to the keyboard and this module in your `config/west.yml` file. 
See my personal [ZMK Config](https://github.com/peterjc/zmk-config) as an example.

## More Info

Read through the [ZMK Module Creation](https://zmk.dev/docs/development/module-creation)
page for background.

For more info on modules as used in ZMK, you can read through the [Zephyr modules
page](https://docs.zephyrproject.org/3.5.0/develop/modules.html) and [ZMK's page
on using modules](https://zmk.dev/docs/features/modules). [Zephyr's west manifest
page](https://docs.zephyrproject.org/3.5.0/develop/west/manifest.html#west-manifests)
may also be of use.
