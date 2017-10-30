+from sys import stdin
+from math import *
+
INF = float('inf')
NINF = float('-inf')

def solve(L,H,G,islas):
  islas.sort()
  #print(a)
  ans,low,n = list(),L,0
  while low<H and n!=len(islas):
    mejor,n = n,n+1
    while n!=len(islas) and islas[n][0]<=low:
      if islas[n][0]>islas[mejor][1]:
        mejor = n
      n += 1
    ans.append(mejor)
    low = islas[mejor][1]
  return len(ans)

def main():
	global islas
    n,d = -1,-1
    line = stdin.readline().strip().split()
    contador = 1
    while len(line)!=0:
        islas = []
        n,d = int(line[0]), int(line[1])
        if n!=0 and d!=0:
            for i in range(n):
                temporal = 1
                x,y = [ int(i) for i in stdin.readline().split() ]
                det = pow(d,2)-pow(y,2)## pitagoras
                if y>d or det<0:
                    temporal = 0
                elif d==y:
                    a,b = x-d,x+d
                else:
                    a,b = x-sqrt(det), x+sqrt(det)
                islas.append([a,b])
            if temporal==1:
                print('Case ',contador,': 'str(solve(0,n,d,islas)))
            elif temporal==0:
                print('Case ',contador,': ','-1')
            contador+=1
            line = stdin.readline()
        line = stdin.readline().strip().split()
main()