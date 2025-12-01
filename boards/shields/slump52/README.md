# Slump52 keyboard firmware

This is firmware for a Raspberry Pi Pico PR2040 controller monoblock 52 key design
(split 3x5 - three rows of five, with thumb keys, cursors, and numpad),
[my curvy Slump52 keyboard](https://codeberg.org/peterjc/pico-keyboards/src/branch/main/slump52).
This is a *diode-free* design with a sparse 13 by 13 scanning matrix designed using the
[Incidence graph of the projective plane of order 3, PG(2,3)](https://houseofgraphs.org/graphs/44089)
(using only 26 vertices or GPIO pins, with 52 edges or keys - see this
[blog post](https://astrobeano.blogspot.com/2025/05/topology-meets-custom-keyboard-circuit.html)
for background.

This matrix shows the 13×13 PG(2,3) bipartite scanning matrix in Paige-Wexler
normal form. The keys are assign so the scanning column order roughly matches
the physical columns (starting with Escape, A, Z, tab as the first column), with
the scanning rows sorted to ensure Escape is top left as the first matrix entry.
The allocation of keys to matrix elements and scanning matrix rows and columns
to GPIO pins was arbitrary and down to how easy it was to layout the PCB traces:

| GP |  28 |  26 | 16 | 15 |  8 |  7 |  6 |  5 |  4 |  3 |  2 |  1 |   O   |
|---:|:---:|:---:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:-----:|
| 27 | Esc |  W  |  E |  R |    |    |    |    |    |    |    |    |       |
| 22 |  Q  |     |    |    | T  |  Y |  U |    |    |    |    |    |       |
| 21 |  A  |     |    |    |    |    |    |  I |  O |  P |    |    |       |
| 20 |  Z  |     |    |    |    |    |    |    |    |    | 7  |  8 |   9   |
| 19 |     |  S  |    |    | T1 |    |    |  K |    |    | 4  |    |       |
| 18 |     |  X  |    |    |    |  H |    |    |  L |    |    |  5 |       |
| 17 |     | Tab |    |    |    |    |  J |    |    | += |    |    |   6   |
| 14 |     |     | D  |    | T2 |    |    |    |  . |    |    |    |   3   |
| 13 |     |     | C  |    |    |  N |    |    |    |  - | 1  |    |       |
| 12 |     |     | V  |    |    |    |  M |  , |    |    |    |  2 |       |
| 11 |     |     |    |  F | T3 |    |    |    |    |  / |    |  0 |       |
| 10 |     |     |    |  G |    |  ← |    |  ↑ |    |    |    |    | Enter |
|  9 |     |     |    |  B |    |    |  ↓ |    |  → |    |  * |    |       |

The keys here are labeled as per Qwerty, with T1, T2, and T3, for the thumbs,
plus the cursors (in a standard inverted-tee layout, not a row):

| Esc |  Q  | W | E | R | T |    |    |    | Y | U | I | O | P | += | 7 | 8 | 9     |
|:---:|:---:|:-:|:-:|:-:|:-:|:--:|:--:|:--:|:-:|:-:|:-:|:-:|:-:|:--:|:-:|:-:|:-----:|
|     |  A  | S | D | F | G |    |    |    | H | J | K | L | - |    | 4 | 5 | 6     |
|     |  Z  | X | C | V | B |    |    |    | N | M | , | . | / |    | 1 | 2 | 3     |
|     | Tab |   |   |   |   | T1 | T2 | T3 | ← | ↓ | ↑ | → | * |    | 0 |   | Enter |

This default layout replaces Qwerty semicolon/colon with hyphen/underscore (for
use with the numpad as minus), adds an extra key below slash/question-mark (used
for division with the numpad) for multiplication, and places the equals-sign/plus
key at the top of this column (but with plus by default and equals with shift).

The suggested thumb keys are backspace, shift, and space. The keys labeled as
`Tab` (left) and `*` (right) could be used as a pinky shift instead (or when held).

Most of the symbols can be used with shift and the numpad, but this and the
remaining punctuation (semicolon, brackets, backslash, pipe, hash, tilde, etc)
can be placed on layers or combos when personalising the layout.

The ZMK Studio unlock combo is Escape (top left) and Numpad 9 (top right):

![Slump52 in ZMK Studio](https://private-user-images.githubusercontent.com/63959/520959351-25bf5275-5e88-483e-8d87-247e24b43555.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjQ2MTY3MDksIm5iZiI6MTc2NDYxNjQwOSwicGF0aCI6Ii82Mzk1OS81MjA5NTkzNTEtMjViZjUyNzUtNWU4OC00ODNlLThkODctMjQ3ZTI0YjQzNTU1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEyMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMjAxVDE5MTMyOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWEzZGE1OGM3MjFlZWM4OTc3MDQxODZiYzlmY2E3MjFkODc2OGU0M2NiZjk5NzJhYzI2MTk0ZDA4ODI0NjQyMmUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0._3ZhYLY2de6tPNHXa-i1H61G-jdCb9BaVv-kVjIh39I)

See also the [QMK TC36K firmware](https://github.com/peterjc/qmk_userspace/tree/main/keyboards/tutte_coxeter_36k),
the [Heawood42 keyboard](https://github.com/triliu/Heawood42) which was the first no-diode
keyboard using graph theory (42 key split design), and the later 56-key monoblock
[JESK56 keyboard](https://github.com/triliu/JESK56).
