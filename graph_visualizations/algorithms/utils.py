import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G, pos=None, highlight_nodes=None, highlight_edges=None, title="Graph"):
    if pos is None:
        pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000)
    if highlight_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes, node_color='orange')
    if highlight_edges:
        nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color='red', width=2)
    plt.title(title)
    plt.show()