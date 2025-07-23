import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    global graph,visited,flag

    for node in graph[x]:
        if visited[x]==visited[node]:
            flag=False
            return
        
        elif visited[node]==0:
            if visited[x]==1: visited[node]=2
            else: visited[node]=1

            dfs(node)


T=int(input())
for _ in range(T):
    v,e=map(int,input().split())

    graph=[[] for _ in range(v+1)]
    visited=[0]*(v+1)
    flag=True

    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        if visited[i]==0:
            visited[i]=1
            dfs(i)

    if flag: print("YES")
    else: print("NO")
    