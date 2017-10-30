from sys import stdin
from collections import deque
# Carlos Arboleda - Camilo Rocha ADA
# se intenta implementar stack ya que se ve como matriz hubo problema
# se implementa con la colas pero no se llega a una solucion para ello se importa de python
# El problema se discutio con Jhonatan Diaz 

# class Stack:
#      def __init__(self):
#          self.items = []
s
#      def isEmpty(self):
#          return self.items == []

#      def push(self, item):
#          self.items.append(item)

#      def pop(self):
#          return self.items.pop()

#      def peek(self):
#          return self.items[len(self.items)-1]

#      def size(self):
#          return len(self.items)

def solve(matriz,num,n,i,j):
	cola=deque()
	opciones=[[0,1],[1,0],[0,-1],[-1,0]]## opciones de vecinos 
	cola.append((i,j))
	contador=0
	while len(cola)!=0:
		i,j=cola.pop()
		if matriz[i][j]!=-1:
			matriz[i][j]=-1
			for temporal in opciones:
				posx,posy=i+temporal[0],j+temporal[1]
				if (posx<n and posx>=0 and posy>=0 and posy<n) and (matriz[posx][posy]==num and[posx,posy] not in cola):
					cola.append((posx,posy))
					contador+=1
	return matriz,contador+1

def main():
	global matriz,k
	k = int(stdin.readline())
	while k!=0:
		matriz = [[0]*k for i in range(k)]## se inicializa la matriz
		for i in range(k-1):## de 0-n-1
			lista=[int (x) for x in stdin.readline().split()]## para acceder a todos los indices de la lista
			for j in range(0,len(lista)-1,2):## for que vaya de 2 en 2 por las duplas
				matriz[lista[j]-1][lista[j+1]-1]=i+1
		temporal=0
		for a in range(k-1):
			for b in range(k-1):
				if matriz[a][b]>0:
					matriz,temporal=solve(matriz,matriz[a][b],k,a,b)
					if temporal!=k:
						print("wrong")

			
		if temporal==k:
			print("good")
		k=int(stdin.readline())

main()
