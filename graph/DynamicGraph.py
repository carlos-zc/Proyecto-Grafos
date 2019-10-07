import numpy as np
import math

from graph.GraphPro import GraphPro


class DynamicGraph(GraphPro):
    last_vertex_modified = np.array([])
    last_vertex_action = ""
    last_node_modified = {
        'node': None,
        'source': np.array([]),
        'target': np.array([]),
    }
    last_node_action = ""

    def __init__(self, source=[], target=[], weight=[], directed=True):
        GraphPro.__init__(self, source, target, weight, directed)
        self.clean_vars()

    def clean_vars(self):
        self.last_vertex_modified = np.array([])
        self.last_vertex_action = ""
        self.last_node_modified = {
            'node': None,
            'source': np.array([]),
            'target': np.array([]),
        }
        self.last_node_action = ""