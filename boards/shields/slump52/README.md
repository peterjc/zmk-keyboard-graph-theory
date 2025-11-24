# Slump52 keyboard firmware

This is firmware for a Raspberry Pi Pico PR2040 controller monoblock 52 key design
(split 3x5 - three rows of five, and in total five thumb keys, cursors, and numpad),
[my curvy Slump52 keyboard](https://codeberg.org/peterjc/pico-keyboards/src/branch/main/slump52).
This is a *diode-free* design with a sparse 13 by 13 scanning matrix designed using the
[Incidence graph of the projective plane of order 3, PG(2,3)](https://houseofgraphs.org/graphs/44089)
(using only 26 vertices or GPIO pins, with 52 edges or keys - see this
[blog post](https://astrobeano.blogspot.com/2025/05/topology-meets-custom-keyboard-circuit.html)
for background.

This matrix shows the 13×13 PG(2,3) bipartite scanning matrix in Paige-Wexler
normal form, with the scanning column order roughly matching the physical
columns (starting with Escape, A, Z, tab column first, finishing with the cursors),
and the scannig rows sorted to ensure Escape is top left as the first matrix entry.
The allocation of keys to matrix elements and scanning matrix rows and columns
to GPIO pins was arbitrary and down to how easy it was to layout the PCB traces:

| GP |  28 | 26 | 22 | 21 |  8 |  7 |  6 |  5 |  4 |  3 |  2 |   1   |  O |
|---:|:---:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:-----:|:--:|
| 27 | Esc |  Q |  E |  T |    |    |    |    |    |    |    |       |    |
| 20 |  A  |    |    |    | B  |  Y | U  |    |    |    |    |       |    |
| 19 |  Z  |    |    |    |    |    |    | I  | P  |  7 |    |       |    |
| 18 | Tab |    |    |    |    |    |    |    |    |    | 8  |   9   | x  |
| 17 |     |  W |    |    | T1 |    |    | O  |    |    | 5  |       |    |
| 16 |     |  S |    |    |    |  J |    |    | +  |    |    |   6   |    |
| 15 |     |  X |    |    |    |    | K  |    |    |  4 |    |       | x  |
| 14 |     |    | R  |    | T2 |    |    |    | -  |    |    |       | x  |
| 13 |     |    | D  |    |    |  H |    |    |    |  1 | 2  |       |    |
| 12 |     |    | C  |    |    |    | ,  | L  |    |    |    |   3   |    |
| 11 |     |    |    |  G | T3 |    |    |    |    |  * |    | Enter |    |
| 10 |     |    |    |  F |    |  N |    | .  |    |    |    |       | x  |
|  9 |     |    |    |  V |    |    | M  |    | /  |    | 0  |       |    |

The keys here are labeled as per Qwerty, with T1, T2, and T3, for the thumbs,
plus the cursors (not shown below):

| Esc |  Q  | W | E | R |  T |    |  Y | U | I | O | P | + | 7 | 8 | 9     |
|:---:|:---:|:-:|:-:|:-:|:--:|:--:|:--:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-----:|
|     |  A  | S | D | F |  G |    |  H | J | K | L | - |   | 4 | 5 | 6     |
|     |  Z  | X | C | V |  B |    |  N | M | , | . | / |   | 1 | 2 | 3     |
|     | Tab |   |   |   | T1 | T2 | T3 |   |   |   |   |   | * | 0 | Enter |

See also the [QMK TC36K firmware](https://github.com/peterjc/qmk_userspace/tree/main/keyboards/tutte_coxeter_36k),
the [Heawood42 keyboard](https://github.com/triliu/Heawood42) which was the first no-diode
keyboard using graph theory (42 key split design), and the later 56-key monoblock
[JESK56 keyboard](https://github.com/triliu/JESK56).
