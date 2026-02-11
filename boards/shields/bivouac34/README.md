# Bivouac34 keyboard firmware

This is the default keymap which you would be expected to customise to your needs
with ZMK Studio or otherwise:

![Default keymap for the Slump34t keyboard ZMK firmware](../../../keymap-drawer/bivouac34.svg)

This is firmware for a Raspberry Pi PR2040 (or potentially RP2350) 'Zero' controller
tented monoblock 34 key design, my [Bivouac34 keyboard](https://codeberg.org/peterjc/pico-keyboards/src/branch/main/bivouac34).

This is a *diode-free* design with a sparse 10 by 10 scanning matrix designed using the
[unique 20 vertex girth 6 graph of maximal 34 edges](https://houseofgraphs.org/graphs/55819)
(using only 20 vertices or GPIO pins, with 34 edges or keys with 4KRO - see this
[blog post](https://astrobeano.blogspot.com/2025/05/topology-meets-custom-keyboard-circuit.html)
for background.

This matrix shows the 10×10 sparse bipartite scanning matrix. The keys are assigned so the
scanning column order matches the physical columns (starting with Q, A, and Z as the first
column), with the scanning rows sorted to ensure Q is top left as the first matrix entry.
The allocation of keys to matrix elements and scanning matrix rows and columns
to GPIO pins was arbitrary and down to how easy it was to layout the PCB traces:

| GP |  29 | 14 | 10 | 6 |   1   |   0   | 3 | 9 | 13 | 28 |
|---:|:---:|:--:|:--:|:-:|:-----:|:-----:|:-:|:-:|:--:|:--:|
| 10 |  Q  |  W |  E | R |       |       |   |   |    |    |
| 14 |  A  |    |    |   |   T   |       |   | I |  O |    |
|  0 |  Z  |    |    |   |       |   Y   | U |   |    |    |
|  4 |     |  S |    |   |   G   |       | J |   |    |    |
| 11 |     |    |  D |   | BkSp  |   H   |   |   |    |    |
| 15 |     |    |    | F |       |       | M | K |    |    |
|  5 |     |    |    | V |       | Space |   |   |  L |    |
|  3 |     |    |    | B | LShft |       |   |   |    |  P |
|  7 |     |  X |    |   |       | RShft |   | , |    |  ; |
|  6 |     |    |  C |   |       |       | N |   |  . |  / |

The keys here are labeled as per Qwerty, with B, backspace, left shift,
right shift, space and N for the thumbs.

|  Q  | W | E | R | T    |       |       | Y     | U | I | O | P |
|:---:|:-:|:-:|:-:|:----:|:-----:|:-----:|:-----:|:-:|:-:|:-:|:-:|
|  A  | S | D | F | G    |       |       | H     | J | K | L | - |
|  Z  | X | C | V |      |       |       |       | M | , | . | / |
|     |   |   | B | BkSp | LShft | RShft | Space | N |   |   |   |

This minimal default layout is rendered as an image above.

The ZMK Studio unlock combo is Q (top left) and T (top right of left half).](https://astrobeano.blogspot.com/2025/05/topology-meets-custom-keyboard-circuit.html)

See also the [QMK Slump34t firmware](https://github.com/peterjc/qmk_userspace/tree/main/keyboards/slump34t),
the [Heawood42 keyboard](https://github.com/triliu/Heawood42) which was the first no-diode
keyboard using graph theory (42 key split design), and the later 56-key monoblock
[JESK56 keyboard](https://github.com/triliu/JESK56).
