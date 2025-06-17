import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur,start,arr,visited):
    # 이미 방문한 경우
    if visited[cur]:
        # 본인이 본인을 선택한 경우
        if cur==start:
            return
        
        # start부터 cur 이전까지는 팀 생성 불가능
        while start!=cur:
            visited[start]=-1
            start=arr[start]

        return
    
    visited[cur]=1
    dfs(arr[cur],start,arr,visited)

T = int(input())

for _ in range(T):
    n=int(input())
    arr = [0] + list(map(int, input().split()))

    # 0: 방문 X, 1: 팀 생성 가능, -1: 팀 생성 불가능
    visited=[0]*(n+1)

    for i in range(1, n+1):
        if visited[i]==0:
            start=i
            dfs(i,start,arr,visited)

    cnt=0
    for i in range(1, n+1):
        if visited[i]!=1:
            cnt+=1

    print(cnt)