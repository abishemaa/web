#pg.py
import networkx as nx
import json

with open('interactions.json', 'r') as file:
    data.load(file)

def interactions (file):

    G = nx.Graph()

    for inter in interactions:
        d1 = inter['drug_a']
        d2 = inter['drug_b']
    return

    G.add_node(d1)
    G.add_node(d2)
    G.add_edge(d1,d2)


