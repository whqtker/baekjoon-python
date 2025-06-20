import sys
input=sys.stdin.readline

n=int(input())
min_value=1e7+1
arr=[[] for _ in range(n)]
visited=[0]*n

def dfs(cur,cnt,val):
    global min_value
    
    if cur>=min_value:
        return
    
    if cnt==n:
        if arr[cur][0]:
            min_value=min(min_value,val+arr[cur][0])

    for i in range(n):
        if arr[cur][i] and not visited[i]:
            visited[i]=1
            dfs(i,cnt+1,val+arr[cur][i])
            visited[i]=0

arr=[list(map(int, input().split())) for _ in range(n)]

visited[0]=1
dfs(0,1,0)

print(min_value)