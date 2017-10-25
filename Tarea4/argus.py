from heapq import *
from sys import stdin
## Carlos Saul Arboleda-Camilo Rocha-ADA 
## ARGUS
## se busca la libreria heap en python y se estudia que hace cada funcion , el programa termina de leer el .in cuando encuentra un # 
## se utiliza el join para imprimir todo de una vez y no con un print para linea por linea 
## se discutio con  Andres Felipe Achury - Mario Bolanos- Jhonatan Diaz

def solve(dupla): ## recibe la dupla queries y las ejecuciones
    queries, k = dupla
    heap = [] ## monton vacio para ir metiendo
    for q in queries:
        heappush(heap, [int(q[1]), int(q[0]), int(q[1])])
    results = [] ## lista vacia para ir metiendo los resultados para luego imprimirlos
    for i in range(int(k)):
        q = heappop(heap) ## saco lo del heap 
        results.append(q[1])
        q[0] += q[2]
        heappush(heap, q)
    return '\n'.join(str(e) for e in results) ## truco del profesor para imprimir todo de una

def main():
    global registros,Ejecuciones,queries,a ## para utilizarlos arriba
    imp = stdin
    a = imp.readline().split()
    queries = []
    while (a != ["#"]): ## condicion de parada dicha por el texto
        queries.append([(a[1]),(a[2])])
        a = imp.readline().split()## leo y parto 
    Ejecuciones = imp.readline().strip()
    registros = (queries,Ejecuciones)
    print(solve(registros))    
main()
