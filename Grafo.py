from graph.Graph import Graph
from algoritmos.dijkstra import *
from algoritmos.floyd_warshall import *

origenes = []
destinos = []
distancias = []

tipo = int(input("Indique el tipo de grafo [1:grafo simple, 2:digrafo]: "))
arist = int(input("Indique la cantidad de aristas (conexiones) que contiene el grafo: "))

print("\n*** INGRESAR DATOS DEL GRAFO ***\n")
if tipo == 1:
    print("# EJEMPLO: El vertice 1 conecta con el vertice 2 y la distancia es de 4")
    for i in range(arist):
        origen = int(input("El vertice: "))
        destino = int(input("conecta con el vertice: "))
        distancia = int(input("y la distancia es de: "))
        print()

        #Guardando los datos en listas
        origenes.append(origen)
        destinos.append(destino)
        distancias.append(distancia)

        #Guardamos la distancia en ambos sentidos ya que es grafo simple
        origen2 = destino
        destino2 = origen
        origenes.append(origen2)
        destinos.append(destino2)
        distancias.append(distancia)

elif tipo == 2:
    print("# EJEMPLO: Del vertice 1 al vertice 2 la distancia es de 4")
    for i in range(arist):
        origen = int(input("Del vertice: "))
        destino = int(input("al vertice: "))
        distancia = int(input("la distancia es de: "))
        print()

        #Guardando los datos en listas
        origenes.append(origen)
        destinos.append(destino)
        distancias.append(distancia)

print("<===== Grafo =====>\n")

grafo = Graph(origenes, destinos, distancias)
grafo.print_r()

while True:
    origen = int(input("\nElija el vertice de origen: "))
    if not(origen in grafo.vertex):
        print("* El vertice elegido no existe, ingrese nuevamente")
    else:
        break

dist = Dijkstra(origen, grafo)
print("\nDistancias Mínimas por Dijsktra: ")
for i in range(len(grafo.vertex)):
    print(f"La distancia mínima de '{origen}' a '{grafo.vertex[i]}' es: {int(dist[i])}")
print(dist)
print()

dist = Dijkstra_apsp(grafo)
print(dist)
print()

dist = Floyd_Warshall(grafo)
print(dist)
print()

grafo.draw()