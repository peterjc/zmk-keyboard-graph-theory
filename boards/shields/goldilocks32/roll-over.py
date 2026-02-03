#!/usr/bin/env python3
"""Analysis of 4 or 6-key roll-over in Hesse Configuration Incidence Graph keyboard.

Graph logged as https://houseofgraphs.org/graphs/56260
"""

import numpy as np
import networkx as nx
from networkx.algorithms import bipartite
from scipy import sparse

rows = 8 + 1  # 8 for the core graph, plus 1 for the nav button
cols = 16
layout_string = """
            RC(0,0) RC(0,1)  RC(0,2) RC(0,3)  RC(4,4)          RC(6,11) RC(5,12) RC(6,13) RC(5,14) RC(2,15)
            RC(1,0) RC(2,1)  RC(3,2) RC(4,3)  RC(7,4)          RC(4,11) RC(4,12) RC(1,13) RC(1,14) RC(6,15)
            RC(7,5) RC(1,5)  RC(2,6) RC(7,6)                            RC(5,9)  RC(3,9)  RC(3,10) RC(6,10)
            RC(8,12) RC(8,6) RC(8,13) RC(8,7) RC(8,3)
                                     RC(3,7)  RC(7,7)          RC(5,8)  RC(2,8)
"""  # from ZMK bivouac34-layouts.dtsi

layout_keys = """
                &kp Q &kp W &kp E &kp R  &kp T                  &kp Y &kp U &kp I     &kp O   &kp P
                &kp A &kp S &kp D &kp F  &kp G                  &kp H &kp J &kp K     &kp L   &kp SEMI
                &kp Z &kp X &kp C &kp V                               &kp M &kp COMMA &kp DOT &kp SLASH
                &kp UP &kp LEFT &kp ENTER &kp RIGHT &kp DOWN
                                  &kp B  &kp BSPC           &kp SPACE &kp N
"""  # from ZMK bivouac34.keymap
layout_keys = """
                &kp Q &kp W &kp E &kp R  &kp T                  &kp Y &kp U &kp I     &kp O   &kp P
                &kp A &kp S &kp D &kp F  &kp G                  &kp H &kp J &kp K     &kp L   &kp SEMI
                &kp Z &kp X &kp C &kp V                               &kp M &kp COMMA &kp DOT &kp SLASH
                &kp UP &kp LEFT &kp ENTER &kp RIGHT &kp DOWN
                                  &kp 1  &kp 2                  &kp 3 &kp 4
"""  # with thumbs renamed as 1 to 4
pretty_chars = {
    "DOT": ".",
    "COMMA": ",",
    "SLASH": "/",
    "SEMI": ";",
    "LGUI": "⌘",
    "TAB": "↹",
    "BSPC": "⌫",
    "LSHFT": "⇧",
    "RSHFT": "⇪",  # really the caps lock symbol
    "SPACE": "⎵",
    "RETURN": "⏎",
    "UP": "⏶",
    "LEFT": "⏴",
    "ENTER": "⏺",
    "RIGHT": "⏵",
    "DOWN": "⏷",
}  # see keymap_drawer.config.yaml
thumbs = "B⌫⇧⇪⎵N"
thumbs = "1234"


def parse_zmk_map(rc_layout, keys_layout, rows, cols):
    # matrix = np.zeros((rows, cols), np.dtypes.StringDType)
    matrix = np.zeros((rows, cols), str)  # single char!
    keys = keys_layout.split()
    for text in rc_layout.split():
        assert text.startswith("RC(") and text.endswith(")") and text.count(",") == 1, (
            text
        )
        action = keys.pop(0)
        assert action == "&kp", action
        k = keys.pop(0)
        # print(text[3:-1], k)
        matrix[tuple(int(_) for _ in text[3:-1].split(","))] = pretty_chars.get(k, k)
    return matrix


pretty_matrix = parse_zmk_map(layout_string, layout_keys, rows, cols)
bipartite_matrix = pretty_matrix.astype(np.bool)
G = bipartite.from_biadjacency_matrix(sparse.csc_array(bipartite_matrix))

import tempfile

print("As a graph6 string:")
with tempfile.NamedTemporaryFile(delete=False) as f:
    nx.write_graph6(G, f.name, header=False)
    _ = f.seek(0)
    print(f.read().decode())

print(bipartite_matrix.astype(int))
print("Markdown matrix")
print("|R/C|" + "|".join(f"{_:<3}" for _ in range(cols)) + "|")
print("|---|" + "---|" * cols)
print(
    "|"
    + " | \n|".join(
        f"R{r:<2}| " + " | ".join(_ if _ else " " for _ in row)
        for r, row in enumerate(pretty_matrix)
    )
    + " |"
)

print("Problem cycles of up to six keys;")
for cycle in nx.chordless_cycles(G, 6):
    classes = [G.nodes[_]["bipartite"] for _ in cycle]
    if len(classes) == 4 and classes == [1, 0, 1, 0]:
        keys = {
            pretty_matrix[cycle[1], cycle[0] - rows],
            pretty_matrix[cycle[1], cycle[2] - rows],
            pretty_matrix[cycle[3], cycle[2] - rows],
            pretty_matrix[cycle[3], cycle[0] - rows],
        }
    elif len(classes) == 4 and classes == [0, 1, 0, 1]:
        keys = {
            pretty_matrix[cycle[0], cycle[3] - rows],
            pretty_matrix[cycle[0], cycle[1] - rows],
            pretty_matrix[cycle[2], cycle[1] - rows],
            pretty_matrix[cycle[2], cycle[3] - rows],
        }
    else:
        assert classes == [1, 0, 1, 0, 1, 0], classes  # col, row, ...
        keys = {
            pretty_matrix[cycle[1], cycle[0] - rows],
            pretty_matrix[cycle[1], cycle[2] - rows],
            pretty_matrix[cycle[3], cycle[2] - rows],
            pretty_matrix[cycle[3], cycle[4] - rows],
            pretty_matrix[cycle[5], cycle[4] - rows],
            pretty_matrix[cycle[5], cycle[0] - rows],
        }
    print(
        "".join(sorted(keys)),
        "left-home" if len(set("ASDF").intersection(keys)) > 1 else "",
        "right-home" if len(set("JKL;").intersection(keys)) > 1 else "",
        "both-thumbs"
        if set(thumbs[:3]).intersection(keys) and set(thumbs[3:]).intersection(keys)
        else "",
        "ignored as opposite arrows"
        if ("⏶" in keys and "⏷" in keys) or ("⏴" in keys and "⏵" in keys)
        else "",
    )
