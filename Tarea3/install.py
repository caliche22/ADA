from sys import stdin
from math import *
# Carlos Arboleda ADA Camilo Rocha 
# Install 
# se hace uso de Activity Scheduling de la clase y se saca un arreglo con el numero de radares x-d y x+d
#donde d es uno de los  catetos del triangulo es decir se hace uso de la libreria math para calcularlo
# con pow y sqrt y sus respectivas condiciones d==y , d!=y d<y o cateto<0 en un plano (x,y)

def solve(islas): ### algoritmo de Activity 
  islas.sort(key=lambda x : x[1])
  ans,n,N = 0,0,len(islas)
  while n!=N:
    mejor,n,ans = n,n+1,ans+1
    while n!=N and islas[n][0]<islas[mejor][1]:
      n += 1
  return ans

def main():
    global islas
    contador = 1
    inp=stdin
    line =inp.readline()
    n,d=[int(j) for j in line.split()]
    while(n!=0 and d!=0):
        islas = []
        temporal=False
        for i in range(n):
            x,y = [ int(i) for i in inp.readline().split() ]
            cateto = pow(d,2)-pow(y,2)## pitagoras pow(d,2) (y,2) o puede ser d**2 y**2
            if d<y or cateto<0: ## condicion 1
                temporal = True
            elif d==y: ## condicion 2
                a,b = x-d,x+d
                islas.append([a,b])
            else: ## condicion 3 
                a,b = x-sqrt(cateto), x+sqrt(cateto)
                islas.append([a,b])
        if temporal==False:
            print("Case "+str(contador)+': '+str(solve(islas)))#se hace uso de la concatenacion + casteando
        else:
            print("Case "+str(contador)+': '+'-1')#se hace uso de la concatenacion + casteando
        contador+=1
        line =inp.readline()
        n,d=[int(j) for j in inp.readline().split()]
main()