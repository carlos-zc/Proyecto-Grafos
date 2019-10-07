from graph.DynamicGraph import DynamicGraph
import numpy as np


class Graph(DynamicGraph):

    def __init__(self, source=[], target=[], weight=[], directed=True):
        DynamicGraph.__init__(self, source, target, weight, directed)

    def print_r(self):
        print("Origen:    ", self.source)
        print("Destino:   ", self.target)
        print("Distancia: ", self.weight)
        print("Vertices:  ", self.vertex)

    def get_weight(self, n1, n2):
        if n1 == n2:
            return 0
        w = self.weight[np.logical_and(self.source == n1, self.target == n2)]
        return np.inf if w.size == 0 else w[0]

    def export(self):
        array_export = [(int(self.source[i]), int(self.target[i]), self.weight[i]) for i in range(self.source.size)]
        return array_export