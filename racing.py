from sys import stdin
# Carlos Saul Arboleda - ADA - Camilo Rocha
# se implementa conjuntos disjuntos y pero hay un problema con el accert no se alcanzo a corregir
# El problema se discutio con Mario Bolanos y Andres Felipe Achury
# Incompleto
# luego se implemento Kruskal con la clase de conjuntos disjuntos 
class dforest(object):
  def __init__(self,size=100):
    """create an emtpy forest"""
    self.__parent = [ i for i in range(size) ]
    self.__size = [ 1 for i in range(size) ]
    self.__rank = [ 0 for i in range(size) ]
    
  def __str__(self):
    """return the string representation of the forest"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return len(self.__parent)
  
  def __contains__(self,x):
    """return if x is an element of the forest"""
    return 0 <= x < len(self)

  def find(self,x):
    """return the representative of the tree of x"""
    assert x in self
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]

  def union(self,x,y):
    """make the union of the trees of x and y"""
    assert x in self and y in self
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      nx,ny = self.__rank[rx],self.__rank[ry]
      if nx<=ny:
        self.__parent[rx] = ry
        self.__size[ry] += self.__size[rx]
        if nx==ny: self.__rank[ry]+=1
      else:
        self.__parent[ry] = rx
        self.__size[rx] += self.__size[ry]
        
  def size(self,x):
    """return the size of the tree of x"""
    assert x in self
    return self.__size[self.find(x)]

def kruskal(G):
  """G is a connected graph in adjacency list representation. For each
  vertex u in G, G[u] is the list of pairs (v0,w0),...(vn,wn) such that
  there is an edge between u and vi with weight wi (0 <= i <= n)"""
  edges = list()
  for i in range(len(G)):               # collect the edges in G
    for v,w in G[i]:
      edges.append((i,v,w))
  # sort the edges in ascending order w.r.t weights in the edges
  edges.sort(key=lambda x: x[2],reverse=True)        
  ans,sans = [ list() for i in range(len(G)) ],0
  df = dforest(len(G))
  i = 0
  while i!=len(edges):
    u,v,w = edges[i]
    if df.find(u)!=df.find(v):
      ans[u].append((v,w)) ; ans[v].append((u,w)) ; sans += w
      df.union(u,v)
    i += 1
  return sans



def main():
  k = int(stdin.readline())
  for j in range(k):
    n,m = [int(x) for x in stdin.readline().split()]
    grafo,temp = [list() for i in range(n)],0
    for y in range(m):
      prueba = [int(u) for u in stdin.readline().split()]
      temp+=prueba[2]
      grafo[prueba[0]-1].append((prueba[1]-1,prueba[2]))
    t=kruskal(grafo)
    print(temp-t)
main()
