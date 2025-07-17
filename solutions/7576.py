import sys
from collections import deque

input=sys.stdin.readline

m,n=map(int,input().split())

queue=deque()
graph=[]

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if row[j] == 1:
            queue.append((i, j))


dx=[-1,0,1,0]
dy=[0,1,0,-1]

while queue:
    x,y=queue.popleft()

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            graph[nx][ny]=graph[x][y]+1
            queue.append((nx,ny))

for row in graph:
    if 0 in row:
        print(-1)
        break
else:
    print(max(map(max, graph))-1)
