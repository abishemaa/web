#pg.py
import networkx as nx
import matplotlib.pyplot as plt
import json

with open('interactions.json', 'r') as file:
    data = json.load(file)


def build_graph(data):

    G = nx.DiGraph()

    severity_map = {
        "Minor": 1,
        "Moderate": 2,
        "Major": 3,
        "Contraindicated": 4
    }

    for inter in data:
        d1 = inter['drug_a']
        d2 = inter['drug_b']

        G.add_edge(
            d1,
            d2,
            interaction=inter['interaction_type'],
            weight=severity_map.get(inter['severity'], 0)
        )

    return G


def draw_graph(G):

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True)

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()


G = build_graph(data)

print("Nodes:", G.nodes())
print("Edges:", G.edges(data=True))

draw_graph(G)