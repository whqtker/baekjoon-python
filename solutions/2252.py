import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())

graph=[[] for _ in range (n+1)]
inDegree=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    inDegree[b]+=1

queue=deque()
for i in range(1,n+1):
    if not inDegree[i]:
        queue.append(i)

while queue:
    x=queue.popleft()
    print(x,end=" ")

    for y in graph[x]:
        inDegree[y]-=1

        if not inDegree[y]:
            queue.append(y)
