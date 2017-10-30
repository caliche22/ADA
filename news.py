from sys import stdin
from collections import deque



def bfs(amigos,principal):
	visitados=[False for i in range(len(amigos))];visitados[principal]=True## marco el primero como visitado
	cola=deque()
	cola.append(principal)
	sacado=0
	# while len(cola)!=0:
	# 	sacado=cola.pop()
	# 	for j in range(len(amigos[sacado])):
	# 		if visitados[index]==0:
	# 			visitados[index]=visitados[sacado]+1
	# 			cola.append(index)
				








def main():
	global amigos,principal,amigos2
	k= int(stdin.readline())
   	amigos = [list() for i in range(k)]
   	for i in range(k):
   		amigos2=[int(x) for x in stdin.readline().strip().split()]
   		for j in range(1,len(amigos2)):
   			amigos[i].append(amigos2[j])
   	print(amigos)
   	#print(amigos2)
   	l=int(stdin.readline())
   	for m in range(l):
   		principal=int(stdin.readline())
   		#bfs(amigos,principal)

main()