import sys
import heapq
input=sys.stdin.readline

n,m=map(int,input().split())
start=int(input())

graph=[[] for _ in range(n+1)]

inf=300001
dist=[inf]*(n+1)
dist[start]=0

for _ in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))

q=[]
heapq.heappush(q,(0,start))
while(q):
    w,cur=heapq.heappop(q)

    if dist[cur]<w:
        continue

    for nxt,nw in graph[cur]:
        if w+nw<dist[nxt]:
            dist[nxt]=w+nw
            heapq.heappush(q,(dist[nxt],nxt))

for d in dist[1:]:
    if d==inf:
        print("INF")
    else:
        print(d)