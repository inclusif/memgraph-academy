import pprint as pp

import matplotlib.pyplot as plt
import networkx as nx

g = nx.read_edgelist(
    "gapd-2022/1-networkX-basics/2-graph-algorithms/data/graph-weighted.txt",
    nodetype=str,
    data=(("weight", int),),
    create_using=nx.Graph(),
)

pos = nx.planar_layout(g)

nx.draw(
    g,
    pos,
    with_labels=True,
    node_color="#f86e00",
    node_size=1000,
    font_weight="bold",
    font_size=20,
)
# nx.draw_networkx_edge_labels(g, pos,edge_labels=edge_labels)

p1 = nx.shortest_path(g, source="go", weight="weight")
p1to6 = nx.shortest_path(g, source="go", target="i", weight="weight")
length = nx.shortest_path_length(g, source="go", target="i", weight="weight")

lengths = nx.shortest_path_length(g, source="go", weight="weight")

print("The shortest path from GO to each node is: ")
results = {a: list(b) for a, b in p1.items()}
pp.pprint(results)
print(lengths)
print("The shortest path from GO to I is ", p1to6, "With length of:", length)

plt.show()
