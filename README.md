# ZMK Firmware for Graph Theory based keyboards

A ZMK module holding a collection of keyboard firmware for [my keyboard (or alternative
keyboard PCB) designs](https://codeberg.org/peterjc/pico-keyboards).
These use Graph Theory based sparse scanning matrices to avoid ghosting, rather than diodes.
They have simple minimal Qwerty layouts including ZKM Studio support to cover basic usage:

* [Gamma Omega TC36K](boards/shields/tc36k), using a Raspberry Pi Pico controller with
  26 GPIO pins for 36 keys and 6-key roll-over using a partial Tutte-Coxeter Graph.
* [Gamma Omega Hesse](boards/shields/hesse), using a Nice!Nano v2 (or clone) controller with
  21 GPIO pins for 36 keys and 4-key roll-over using the Hesse Configuration Incidence Graph.
* [Forager Acid](boards/shields/acid), a Bluetooth split keyboard using a Seeed Xiao NRF52840
  controller with 13 GPIO pins for 17 keys and 4-key roll-over per half using a partial Heawood Graph.
* [Slump52](boards/shields/slump52), using a Raspberry Pi Pico controller with
  26 GPIO pins for 52 keys and 4-key roll-over using the Incidence Graph of the
  Projective Plane of order 3 PG(2,3).
* [Bivvy16D](boards/shields/bivvy16d), a Bluetooth *or wired* split keyboard using
  17 GPIO pins for 16 (or 15) keys and a 5-way directional button on each half,
  with 4-key roll-over per half (14KRO without the navigation button).
* [Bivouac34](boards/shields/bivouac34), using a Wareshare RP2040-Zero controller with
  20 GPIO pins for 34 keys and 4-key roll-over using the unique but unnamed graph of this size.

See also my [QMK keyboard firmware](https://github.com/peterjc/qmk_userspace), and the
following ZMK keyboard firmware for other people's diode-free Graph Theory designs:

* [Heawood42](https://github.com/triliu/Heawood42/tree/main/zmk/heawood42), the *first*
  diode-free Graph Theory based keyboard. A Bluetooth split keyboard with 14 GPIO pins
  for 21 keys and 4-key roll-over per half using the (full) Heawood Graph.

## Usage

If you had built one of my keyboard PCB designs you can download the [latest build of
firmware for these keyboards](https://github.com/peterjc/zmk-keyboard-graph-theory/releases/tag/latest),
using a default Qwerty layout with ZMK Studio enabled as a starting point.

If you then wanted to customise the firmware, you would probably want to clone the
[Unified ZMK Config Template](https://github.com/zmkfirmware/unified-zmk-config-template),
and include a reference to the keyboard and this module in your `config/west.yml` file:

```yaml
manifest:
  defaults:
    revision: v0.3
  remotes:
    - name: zmkfirmware
      url-base: https://github.com/zmkfirmware
    # *** Add the following two lines: ***  
    - name: peterjc
      url-base: https://github.com/peterjc
    # *** Add the above two lines ***
  projects:
    - name: zmk
      remote: zmkfirmware
      revision: v0.3
      import: app/west.yml
    # *** Add the following three lines: ***
    - name: zmk-keyboard-graph-theory
      remote: peterjc
      revision: v0.3
    # *** Add the above three lines ***
  self:
    path: config
```

Add your desired keymap using the appropriate naming (`tc36k`, `hesse`, `acid`, `slump52`,
`bivvy16d`, `bivouac34`, etc) which needs at least one file like `config/tc36k.keymap`, and
add a matching entry to your `build.yaml` with the appropriate controller board (like
`rpi_pico` for the `tc36k`), eg:

```yaml
include:
  - board: rpi_pico
    shield: tc36k
    snippet: studio-rpc-usb-uart
    cmake-args: -DCONFIG_ZMK_STUDIO=y
```

Split keyboards get both left and right (and dongle) entries in `build.yaml`.
If GitHub Actions are turned on, this should then build your new firmware.

Note the explicit pin to ZMK v0.3 (and my [v0.3 branch](https://github.com/peterjc/zmk-keyboard-graph-theory/tree/v0.3)).
With this you should use the older ZMK specific board names of
`seeeduino_xiao_ble`, `nice_nano_v2`, or `rpi_pico` in your `build.yaml` file.

In the forthcoming ZMK v0.4 (currently the `main` branch of ZMK, and targeted by
my `main` branch here), there have been breaking changes including the board names
(which are now all defined as ZMK variants of the underlying versioned Zephyr
boards) and details like how to use the Xiao's NFC pads as GPIOs.
If you want to track `main` then you should use the new board names of
`xiao_ble//ZMK`, `nice_nano@2.0.0//ZMK`, or `rpi_pico//ZMK` in your `build.yaml`
file. It would also be wise to join the ZMK Discord and subscribe to the
[ZMK blog](https://zmk.dev/blog) and [ZMK Mastodon](https://fosstodon.org/@zmk).

See my personal [ZMK Config](https://github.com/peterjc/zmk-config) as an example.

## More Info

Read through the [ZMK Module Creation](https://zmk.dev/docs/development/module-creation)
page for background.

For more info on modules as used in ZMK, you can read through the [Zephyr modules
page](https://docs.zephyrproject.org/3.5.0/develop/modules.html) and [ZMK's page
on using modules](https://zmk.dev/docs/features/modules). [Zephyr's west manifest
page](https://docs.zephyrproject.org/3.5.0/develop/west/manifest.html#west-manifests)
may also be of use.
