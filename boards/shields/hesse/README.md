# Gamma-Omega Hesse keyboard firmware

This is firmware for a Bluetooth capable Nice!Nano v2 or Supermini nRF25840 (aka
ProMicro52840) controller monoblock 36 key design (split 3x5_3 - three rows of five,
and three thumb keys, for each hand): the
[Gamma Omega Hesse keyboard](https://github.com/unspecworks/gamma-omega/tree/main/hesse).
This is a *diode-free* design with a sparse 9 by 12 scanning matrix designed using the
[Hesse Configuration Incidence Graph](https://houseofgraphs.org/graphs/44164) (using
all 21 GPIO pins). This is a bipartite graph with 9 (scanning rows) plus 12 (scanning
columns) giving 21 vertices, and 36 edges (keys). The graph is girth 6, meaning sadly
the keyboard has only 4-key roll-over. See this
[blog post](https://astrobeano.blogspot.com/2025/05/topology-meets-custom-keyboard-circuit.html)
for background.

This matrix shows the full 9×12 Hesse Configuration Incidence Graph bipartite
scanning matrix. The allocation of keys to matrix elements and scanning matrix rows
and columns to GPIO pins was arbitrary and down to how easy it was to layout the PCB
traces:

| GPIO| D8 | D7 | D1 | D2 | D6 | D9 | 1.07 | D15 | D18 | D19 | 1.01 | 1.02 |
|:----|:--:|:--:|:--:|:--:|:--:|:--:|:----:|:---:|:---:|:---:|:----:|:----:|
| D0  |  Q |  W |  E |  R |    |    |      |     |     |     |      |      |
| D10 |  Z |    |    |    |  B | L1 |  R3  |     |     |     |      |      |
| D4  |  A |    |    |    |    |    |      |  H  |  U  |  ,  |      |      |
| D3  |    |  S |    |    |  G |    |      |  Y  |     |     |   L  |      |
| D16 |    |  X |    |    |    | L3 |      |     |  M  |     |      |   ;  |
| D14 |    |    |  C |    |    |    |  R2  |  N  |     |     |      |   /  |
| D21 |    |    |  D |    |    | L2 |      |     |     |  I  |   O  |      |
| D5  |    |    |    |  V |    |    |  R1  |     |  J  |     |   .  |      |
| D20 |    |    |    |  F |  T |    |      |     |     |  K  |      |   P  |

The keys here are labeled as per Qwerty, with L1, L2, L3, R3, R2, and R1 for the thumbs:

| Q | W |  E |  R |  T |   |  Y |  U |  I | O | P |
|:-:|:-:|:--:|:--:|:--:|:-:|:--:|:--:|:--:|:-:|:-:|
| A | S |  D |  F |  G |   |  H |  J |  K | L | ; |
| Z | X |  C |  V |  B |   |  N |  M |  , | . | / |
|   |   | L1 | L2 | L3 |   | R3 | R2 | R1 |   |   |

See also the [ZMK TC36K firmware](../hesse/),
[QMK TC36K firmware](https://github.com/peterjc/qmk_userspace/tree/main/keyboards/tutte_coxeter_36k),
the [Heawood42 keyboard](https://github.com/triliu/Heawood42) which was the first no-diode
keyboard using graph theory (42 key split design), and the later 56-key monoblock
[JESK56 keyboard](https://github.com/triliu/JESK56).
