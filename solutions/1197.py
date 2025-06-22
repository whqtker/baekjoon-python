import sys
import heapq
input=sys.stdin.readline

v,e=map(int,input().split())

graph=[[] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

mst=[0]*(v+1)

q=[]
heapq.heappush(q,(0,1))

min_cost=0
while q:
    cost,node=heapq.heappop(q)

    if mst[node]:
        continue

    min_cost+=cost
    mst[node]=1

    for nnode,ncost in graph[node]:
        if not mst[nnode]:
            heapq.heappush(q,(ncost,nnode))

print(min_cost)
