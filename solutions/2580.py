import sys

input=sys.stdin.readline

arr=[list(map(int,input().split())) for _ in range(9)]

target=[]
for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            target.append((i,j))

def check(x,y,k):
    for i in range(9):
        if arr[x][i]==k or arr[i][y]==k:
            return False
    
    area_x=(x//3)*3
    area_y=(y//3)*3

    for i in range(area_x,area_x+3):
        if k in arr[i][area_y:area_y+3]:
            return False
        
    return True

def dfs(cnt):
    if cnt==len(target):
        for row in arr:
            print(*row)

        sys.exit(0)

    x,y=target[cnt]

    for k in range(1,10):
        if check(x,y,k):
            arr[x][y]=k

            dfs(cnt+1)

            arr[x][y]=0

dfs(0)