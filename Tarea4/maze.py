from heapq import *
from sys import stdin
# Carlos Arboleda -Camilo Rocha
# ADA
# Mice and Mace
# Se implementa el algoritmo visto en clase de dystra con heaps aparte de eso se inicializa el grafo por medio de una lista de adyacencia 
# el algoritmo de dystra devuelve una lista [x1.....xn] con los vertices que tienen que recorrer para salir en este caso el raton 
#Se discutio el problema con Andres Valencia - Andres Felipe Achury
INF = float('inf')

def solve(laberinto,salida):
  """G is a graph representation in adjacency list format with vertices
     in the set { 0, ..., |V|-1 } and source a vertex in G"""
  # dist[u] : "minimum distance detected from source to u
  distancia = [ INF for i in range(len(laberinto)) ] ; distancia[salida] = 0
  visitados = [ False for i in range(len(laberinto)) ]
  heap = [ (0,salida) ]
  while len(heap)!=0:
    d,u = heappop(heap)
    if not(visitados[u]):
      visitados[u] = True
      for v,w in laberinto[u]:
        if distancia[v]>d+w:
          distancia[v] = d+w
          heappush(heap,(distancia[v],v))
  return distancia


def main():
	global laberinto,salida 
	distanciaM=[]
	line=stdin.readline()
	while len(line)!=0:
		ncasos=int(line.strip())## numero de casos
		line=stdin.readline()
		for i in range(ncasos):
			contador=0## contados de ratones
			celdas=int(stdin.readline().strip())## numero de celdas
			salida=int(stdin.readline())## numero de la celda
			temporizador=int(stdin.readline().strip())## cuanto tiempo tiene para salir
			arcos=int(stdin.readline().strip())## numero de conexiones
			laberinto=[list() for i in range(arcos+celdas)] ## armar el laberinto " grafo"
			if arcos!=0:
				for m in range(arcos):
					l,m,t=[int(x) for x in stdin.readline().split()]
					camino=[l,t]
					laberinto[m].append(camino)
				print(laberinto)
				distanciaM=solve(laberinto,salida)## dystra devuelve una lista
				for n in range(len(distanciaM)):
					if distanciaM[n]<=temporizador:
						contador+=1
			else:
				contador+=1
			if i!=ncasos-1:
				print(contador)
				print("")
			else:
				print(contador)
			line=stdin.readline()
main()