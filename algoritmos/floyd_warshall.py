import numpy as np

def Floyd_Warshall(grafo):

    total_vertices = len(grafo.vertex)
    dist = np.zeros((total_vertices, total_vertices))
    dist.fill(np.inf)

    for idx in range(grafo.source.size):
        index_s = grafo.vertex == grafo.source[idx]
        index_t = grafo.vertex == grafo.target[idx]
        dist[index_s, index_t] = grafo.weight[idx]
    for index in range(grafo.vertex.size):
        dist[index, index] = 0

    for k in np.nditer(grafo.vertex):
        for i in np.nditer(grafo.vertex):
            for j in np.nditer(grafo.vertex):
                index_k = grafo.vertex == k
                index_i = grafo.vertex == i
                index_j = grafo.vertex == j

                if dist[index_i, index_j] > dist[index_i, index_k] + dist[index_k, index_j]:
                    dist[index_i, index_j] = dist[index_i, index_k] + dist[index_k, index_j]

    return dist
