import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class GraphPro:
    source = []
    target = []
    weight = []
    vertex = []

    undirected = 0

    def __init__(self, source=[], target=[], weight=[], directed=True):
        self.directed = directed
        self.source = np.array(source)
        self.target = np.array(target)
        self.weight = np.array(weight)

        if self.directed is False:
            self.source = np.concatenate([self.source, self.target])
            self.target = np.concatenate([self.target, np.array(source)])
            self.weight = np.concatenate([self.weight, self.weight])

        self.set_vertex()

    def set_vertex(self):
        vertex = np.unique(self.source)
        vertex2 = np.unique(self.target)
        self.vertex = np.unique(np.concatenate([vertex, vertex2]))
        return self.vertex

    def draw(self, with_weight=True):
        gr = nx.DiGraph()
        gr.add_weighted_edges_from(self.export())

        list_edges = list(gr.edges())
        list_nodes = list(gr.nodes)
        last = ()
        last_nodes = []

        pos = nx.spring_layout(gr)
        nx.draw_networkx_edges(gr, pos=pos, with_labels=True, edgelist=list_edges, node_size=600)
        nx.draw_networkx_nodes(gr, pos=pos, with_labels=True, nodelist=list_nodes, node_size=600)

        if len(last) > 0:
            nx.draw_networkx_edges(gr, pos=pos, edgelist=[last], width=2.0, edge_color=color)

        if len(last_nodes) > 0:
            color = ''
            color_node = ''

            nx.draw_networkx_nodes(gr, pos=pos, with_labels=True,
                                    node_color=color_node,
                                    node_size=600)
            nx.draw_networkx_edges(gr, pos=pos, edgelist=last_nodes, width=2.0, edge_color=color)

        if with_weight:
            edge_labels = dict([((u, v,), d['weight']) for u, v, d in gr.edges(data=True)])
            nx.draw_networkx_edge_labels(gr, pos=pos, edgelist=list_edges, edge_labels=edge_labels)

        labels = dict()
        for i in list_nodes:
            labels[i] = str(i)
        nx.draw_networkx_labels(gr, pos, labels)

        plt.show()
