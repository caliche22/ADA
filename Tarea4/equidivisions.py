import sys
from numpypy import *







def fillColor(i, j, c):
        directions = [(i, j - 1), (i, j + 1), (i + 1, j), (i - 1, j)] ## poner loos limites de la matriz
        for i1, j1 in directions:
            if i1 > 0 and i1 <= n and j1 > 0 and j1 <= n\
                    and graph[i1, j1] == c and not visited[i1, j1]:
                visited[i1, j1] = 1
                cCount[0] += 1
                fillColor(i1, j1, c)




def testColor(color, count):
	cCount = [1]
    flag = False
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i, j] == color:
                visited[i, j] = 1
                fillColor(i, j, color)
                flag = True
                break
        if flag:
            break
    return cCount[0] == count


def main():