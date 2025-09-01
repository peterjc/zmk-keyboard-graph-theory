# Peter's ZMK Keyboard Firmware

A ZMK module holding a collection of keyboard firmware for my keyboard PCB designs.
They have simple minimal Qwerty layouts including ZKM Studio support to cover basic usage:

* [Gamma Omega TC36K](boards/shields/tc36k), a Graph Theory based diode-free keyboard with
  26 GPIO pins for 36 keys and 6-key roll-over using a partial Tutte-Coxeter Graph.

## Usage

If you had built on of my keyboard PCB designs and wanted to customise the firmware, you
would probably want to clone the [Unified ZMK Config Template](https://github.com/zmkfirmware/unified-zmk-config-template),
and include a reference to the keyboard and this module in your `config/west.yml` file. 

See my personal [ZMK Config](https://github.com/peterjc/zmk-config) as an example.

## More Info

For more info on modules, you can read through  through the [Zephyr modules page](https://docs.zephyrproject.org/3.5.0/develop/modules.html) and [ZMK's page on using modules](https://zmk.dev/docs/features/modules). [Zephyr's west manifest page](https://docs.zephyrproject.org/3.5.0/develop/west/manifest.html#west-manifests) may also be of use.
