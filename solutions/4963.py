import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**6)

dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

def dfs(x,y):
    global graph, visited

    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<h and 0<=ny<w and visited[nx][ny]==0 and graph[nx][ny]==1:
            visited[nx][ny]=1
            dfs(nx,ny)

while True:
    w,h=map(int,input().split())

    if w==0 and h==0:
        break

    graph=[]
    for _ in range(h):
        graph.append(list(map(int,input().split())))

    visited=[[0]*w for _ in range(h)]

    ans=0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and visited[i][j]==0:
                ans+=1
                dfs(i,j)

    print(ans)
