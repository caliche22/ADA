from sys import stdin

## Carlos Saul Arboleda
## Camilo Rocha
## ADA 
## Ants
## Se discutio con Andres Valencia - Jose Reyes 




def solve(largo):
	l,h=0,0
	for i in range(len(lista)):
		j=int(lista[i])
		l=max(l,min((largo-j),j))
		h=max(h,max((largo-j),j))
	print(l,h)

def solve1(largo,n):
	l,h=0,0
	while z!=n:
		j=int(lista[z])
		l=max(l,min((largo-j),j))
		h=max(h,max((largo-j),j))
		z=z+1
	print(l,h)

def main():
	global largo,n,lista
	casos=int(stdin.readline())
	while casos!=0:
		line=stdin.readline()
		largo,n=[int (x) for x in line.split()]
		lista=stdin.readline().split()
		solve(largo)
		casos=casos-1
main()

