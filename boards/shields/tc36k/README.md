# Gamma-Omega T36K (Tutte Coxeter 36 keys)

This is firmware for a Raspberry Pi Pico PR2040 controller monoblock 36 key design
(split 3x5_3 - three rows of five, and three thumb keys, for each hand). This is a
*diode-free* design with a sparse 13 by 13 scanning matrix designed using a partial
[Tutte-Coxeter](https://en.wikipedia.org/wiki/Tutte%E2%80%93Coxeter_graph) graph
(using only 26 vertices or GPIO pins, with 36 edges or keys - see this
[blog post](https://astrobeano.blogspot.com/2025/05/ergo-mech-keyboard-wiring-using-tutte-coxeter-graph.html)
for background, although the final pin selection and trace routing changed).

![Partial Tutte-Coxeter Graph (26/30 vertices, 36/45 edges)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvS5QfAl7YotptMtpu0nG8XOHOsqG2vocUFF2sRgrn_QwAcUQNhDkctHt_42rQor3Bb5tbAW6FiOsYqv2craP086HMTuAqWk9U0A4yOeEsQkhyphenhyphenUxoayJWf5e-N3_Jg1TC1p9YAiVPTK02pEVCUu3hl72REIk5BAjXgZGoF7T-NWQ28iRirwFs6yzFzAe0/w200-h194/Screenshot%202025-05-28%20at%2014.59.35.png)

This matrix shows the full 15×15 Tutte-Coxeter bipartite scanning matrix with the
two unused rows and columns last (❌), and the further 9 keys this would allow (⭕)
if using 30 GPIOs rather than just 26 for a 13×13 scanning matrix. The allocation
of keys to matrix elements and scanning matrix rows and columns to GPIO pins was
arbitrary and down to how easy it was to layout the PCB traces:

| GP | 11 | 10 | 3 | 4 | 7 | 26 | 27 | 28 | 15 | 21 | 19 | 20 | 16 | ❌ | ❌ |
|---:|:--:|:--:|:-:|:-:|:-:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 12 |  / |    |   |   |   |    |  F |    |    |    |    |    |    |    | ⭕ |
| 8  |  P |  L |   |   |   |    |    |    |    |    |    |  A |    |    |    |
| 9  |    |  . | , |   |   |    |    |    |    |    |    |    |    | ⭕ |    |
| 1  |    |    | K | I |   |    |    |    |    |  E |    |    |    |    |    |
| 6  |    |    |   | M | H |    |    |    |    |    |    |    |    |    | ⭕ |
| 2  |    |  U |   |   | Y |  T |    |    |    |    |    |    |    |    |    |
| 22 |    |    |   |   |   |  G |  V |    |    |    |    |    | L3 |    |    |
| 0  |    |    | O |   |   |    |  W |  R |    |    |    |    |    |    |    |
| 13 |    |    |   |   | N |    |    |  D | R2 |    |    |    |    |    |    |
| 14 |  ; |    |   |   |   |    |    |    | R1 |  S |    |    |    |    |    |
| 18 |    |    |   |   |   |  B |    |    |    |  X | L2 |    |    |    |    |
| 17 |    |    |   |   |   |    |    |  C |    |    | L1 |  Z |    |    |    |
| 5  |    |    |   | J |   |    |    |    |    |    |    |  Q | R3 |    |    |
| ❌ |    |    |   |   |   |    |    |    | ⭕ |    |    |    | ⭕  | ⭕ |    |
| ❌ |    |    |   |   |   |    |    |    |    |    | ⭕ |    |    | ⭕  | ⭕ |

The keys here are labeled as per Qwerty, with L1, L2, L3, R3, R2, and R1 for the thumbs:

| Q | W |  E |  R |  T |   |  Y |  U |  I | O | P |
|:-:|:-:|:--:|:--:|:--:|:-:|:--:|:--:|:--:|:-:|:-:|
| A | S |  D |  F |  G |   |  H |  J |  K | L | ; |
| Z | X |  C |  V |  B |   |  N |  M |  , | . | / |
|   |   | L1 | L2 | L3 |   | R3 | R2 | R1 |   |   |

The first physical PCB for this was designed using the [Gamma Omega
keyboard](https://github.com/unspecworks/gamma-omega) footprint from Ergogen.
That is intended for use with the same Raspberry Pi Pico YD-RP2040 microcontroller
board in order to fit the same 3D printed case, including reset button placement.

See also the [QMK TC36K firmware](https://github.com/peterjc/qmk_userspace/tree/main/keyboards/tutte_coxeter_36k),
the [Heawood42 keyboard](https://github.com/triliu/Heawood42) which was the first no-diode
keyboard using graph theory (42 key split design), and the later 56-key monoblock
[JESK56 keyboard](https://github.com/triliu/JESK56).
