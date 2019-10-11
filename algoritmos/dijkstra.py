import numpy as np

def Dijkstra(origen, grafo):

    total_vertices = len(grafo.vertex)
    Q = np.array(grafo.vertex)

    dist = np.zeros(total_vertices)
    dist.fill(np.inf)

    dist[grafo.vertex == origen] = 0

    while len(Q) != 0:

        min = np.inf
        u = 0
        for q in Q:
            if dist[grafo.vertex == q] <= min:
                min = dist[grafo.vertex == q]
                u = q

        Q = np.delete(Q, np.argwhere(Q == u))

        for v in grafo.target[grafo.source == u]:
            alt = dist[grafo.vertex == u] + grafo.get_weight(u, v)
            index_v = grafo.vertex == v
            if alt < dist[index_v]:
                dist[index_v] = alt

    return dist

def Dijkstra_ad(grafo):

    result = np.full((grafo.vertex.size, grafo.vertex.size), np.inf)
    contador = 0
    for v in grafo.vertex:
        result[contador] = Dijkstra(v, grafo)
        contador = contador + 1

    return result
