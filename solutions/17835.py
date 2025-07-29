import sys
import heapq

input=sys.stdin.readline

# 도시의 수, 도로의 수, 면접장의 수
n,m,k=map(int,input().split())

graph=[[] for _ in range(n+1)]

# 면접장을 시작 노드로 역방향으로 다익스트라 알고리즘을 적용한다.
for _ in range(m):
    u,v,c=map(int,input().split())
    graph[v].append((c,u))

q=[]
dist=[sys.maxsize]*(n+1)
start=list(map(int,input().split()))
for s in start:
    dist[s]=0
    heapq.heappush(q,(0,s))

max_dist=-1
city=-1

while q:
    w,cur=heapq.heappop(q)

    if dist[cur]<w:
        continue

    for nw,nxt in graph[cur]:
        if w+nw<dist[nxt]:
            dist[nxt]=w+nw
            heapq.heappush(q,(dist[nxt],nxt))

for i in range(1,n+1):
    if dist[i]!=sys.maxsize and dist[i]>max_dist:
        max_dist=dist[i]
        city=i

print(city)
print(max_dist)
