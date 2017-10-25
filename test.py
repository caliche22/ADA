from sys import stdin
import math

class disjoint(object):
  def __init__(self,size):
    self.__parent = [i for i in range (size)]
    self.__rank = [0 for i in range (size)]

  def findSet(self,x):
    if x != self.__parent[x]:
      self.__parent[x] = self.findSet(self.__parent[x])
    return self.__parent[x]

  def isSameSet(self,x,y):
    return self.findSet(x) == self.findSet(y)

  def union(self,x,y):
    px, py = self.findSet(x), self.findSet(y)
    if px != py:
      if self.__rank[px] > self.__rank[py]:
        self.__parent[py] = px
      else:
        self.__parent[px] = py
        if self.__rank[px] == self.__rank[py]:
          self.__rank[py] += 1

def distance(x1,y1,x2,y2):
  dx = x1 -x2
  dy = y1 - y2
  return math.sqrt(dx*dx + dy*dy)

def main():
  cases = int(stdin.readline().strip())
  for i in range(cases):
    stdin.readline()
    n = int(stdin.readline().strip())
    points = []
    edgeList = []
    for j in range(n):
      x ,y = [float(m) for m in stdin.readline().strip().split()]
      points.append((x,y))
      if j > 0:
        for k in range(j):
          d = distance(points[k][0],points[k][1],points[j][0],points[j][1])
          edgeList.append((d,k,j))
          edgeList.append((d,j,k))

    edgeList.sort()
    ds = disjoint(n)
    ans = 0.0
    for e in edgeList:
      if not ds.isSameSet(e[1],e[2]):
        ds.union(e[1],e[2])
        ans += e[0]

    if i > 0:
      print()
    print("{0:.2f}".format(ans))

main()

