from sys import stdin
## se aplica clases como se dijo en clase
## la funcion def comparar es el caso principal de programacion voraz
## Carlos Arboleda-Camilo Rocha - ADA
## Commando
## Se discutio el problema con Andres Felipe Achury - Andres Valencia 
## modelo de como hacer la clase visto en clase


# class soldier(object):
#     def __init__(self,b,j):
#         self.b,self.j = b,j
#     def __lt__(self,other):
#         if self.j!=other.j: return other.j<self.j
#         else: return other.b<self.b
#     def __eq__(self,other):
#         return self.b==other.b and self.j==other.j
#     def __str__(self):
#         return '({0},{1})'.format(self.b,self.j)
class soldados(object):
	def __init__(self,b,j):
			self.b=b
			self.j=j
	def __lt__(self, other):
		if self.j!=other.j:
			return other.j<self.j
		return other.b<self.b

	def __eq__(self, other):
		return self.b==other.b and self.j==other.j

	def __str__(self):
		return '({0},{1})'.format(self.b, self.j)


def solve(soldados):
	soldados.sort()
	soldado1=0
	soldado2=0
	for i in range(len(soldados)):
		soldado1+=soldados[i].b
		if(soldado1+soldados[i].j>soldado2):
			soldado2=soldado1+soldados[i].j
	return soldado2


def main():
	caso=1
	linea=int(stdin.readline())
	while linea!=0:
		casos=0
		temporal=[]
		while(casos<linea):
			b,j=[int (x) for (x) in stdin.readline().split()]
			soldado = soldados(b,j)
			temporal.append(soldado)
			casos+=1
		print("Case "+ str(caso) + ": "+ str(solve(temporal)))
		caso+=1
		linea=int(stdin.readline())

main()

	

