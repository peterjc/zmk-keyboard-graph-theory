#!/usr/bin/env python3
"""Analysis of 4-key roll-over in Hesse Configuration Incidence Graph keyboard."""

import numpy as np
import networkx as nx
from networkx.algorithms import bipartite
from scipy import sparse

rows = 9
cols = 12
layout_string = """
            RC(0,0) RC(0,1) RC(0,2) RC(0,3) RC(8,4) RC(3,7) RC(2,8) RC(6,9) RC(6,10) RC(8,11)
            RC(2,0) RC(3,1) RC(6,2) RC(8,3) RC(3,4) RC(2,7) RC(7,8) RC(8,9) RC(3,10) RC(4,11)
            RC(1,0) RC(4,1) RC(5,2) RC(7,3) RC(1,4) RC(5,7) RC(4,8) RC(2,9) RC(7,10) RC(5,11)
                            RC(1,5) RC(6,5) RC(4,5) RC(1,6) RC(5,6) RC(7,6)
"""  # from ZMK hesse.overlay
layout_keys = """
                &kp Q &kp W &kp E    &kp R   &kp T    &kp Y     &kp U     &kp I     &kp O      &kp P
                &kp A &kp S &kp D    &kp F   &kp G    &kp H     &kp J     &kp K     &kp L      &kp SEMI
                &kp Z &kp X &kp C    &kp V   &kp B    &kp N     &kp M     &kp COMMA &kp DOT    &kp SLASH
                            &kp LGUI &kp TAB &kp BSPC &kp LSHFT &kp SPACE &kp RETURN
"""  # from ZMK hesse.keymap
layout_keys = """
                &kp Q &kp W &kp E    &kp R   &kp T    &kp Y     &kp U     &kp I     &kp O      &kp P
                &kp A &kp S &kp D    &kp F   &kp G    &kp H     &kp J     &kp K     &kp L      &kp SEMI
                &kp Z &kp X &kp C    &kp V   &kp B    &kp N     &kp M     &kp COMMA &kp DOT    &kp SLASH
                            &kp 1    &kp 2   &kp 3    &kp 4     &kp 5     &kp 6
"""  # from ZMK hesse.keymap
pretty_chars = {
    "DOT": ".",
    "COMMA": ",",
    "SLASH": "/",
    "SEMI": ";",
    "LGUI": "⌘",
    "TAB": "↹",
    "BSPC": "⌫",
    "LSHFT": "⇧",
    "SPACE": "⎵",
    "RETURN": "⏎",
}  # see keymap_drawer.config.yaml
thumbs = "↹⌫⇧⎵⏎"
thumbs = "123456"


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
        matrix[tuple(int(_) for _ in text[3:-1].split(","))] = pretty_chars.get(k, k)
    return matrix


pretty_matrix = parse_zmk_map(layout_string, layout_keys, rows, cols)
bipartite_matrix = pretty_matrix.astype(np.bool)
G = bipartite.from_biadjacency_matrix(sparse.csc_array(bipartite_matrix))

print(bipartite_matrix.astype(int))
print(
    "| "
    + " | \n| ".join(" | ".join(_ if _ else " " for _ in row) for row in pretty_matrix)
    + " |"
)

print("Problem cycles of six keys;")
for cycle in nx.chordless_cycles(G, 6):
    classes = [G.nodes[_]["bipartite"] for _ in cycle]
    assert classes == [1, 0, 1, 0, 1, 0], classes  # col, row, ...
    keys = "".join(
        (
            pretty_matrix[cycle[1], cycle[0] - rows],
            pretty_matrix[cycle[1], cycle[2] - rows],
            pretty_matrix[cycle[3], cycle[2] - rows],
            pretty_matrix[cycle[3], cycle[4] - rows],
            pretty_matrix[cycle[5], cycle[4] - rows],
            pretty_matrix[cycle[5], cycle[0] - rows],
        )
    )
    print(
        keys,
        "left-home" if len(set("ASDF").intersection(keys)) > 1 else "",
        "right-home" if len(set("JKL;").intersection(keys)) > 1 else "",
        "both-thumbs"
        if set(thumbs[:3]).intersection(keys) and set(thumbs[3:]).intersection(keys)
        else "",
    )
