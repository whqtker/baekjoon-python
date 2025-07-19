import sys
from collections import deque
import copy
from itertools import combinations

input=sys.stdin.readline

n,m=map(int,input().split())

graph=[]
empty=[]
virus=[]
for i in range(n):
    row=list(map(int,input().split()))
    graph.append(row)

    for j in range(m):
        if row[j]==2:
            virus.append((i,j))

        elif row[j]==0:
            empty.append((i,j))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

combs=combinations(empty,3)
ans=0
for comb in combs:
    tmp_graph=copy.deepcopy(graph)

    for wx,wy in comb:
        tmp_graph[wx][wy]=1

    queue=deque(virus)

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and tmp_graph[nx][ny]==0:
                tmp_graph[nx][ny]=2
                queue.append((nx,ny))

    cur=0
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j]==0:
                cur+=1

    ans=max(cur,ans)

print(ans)