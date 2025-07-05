import sys
input=sys.stdin.readline

n=int(input())
arr=[0]*n # arr[i]=x: i번째(i행) 퀸은 x번째 열에 위치한다.
ans=0

# 퀸은 각 행 또는 열, 대각선에 하나만 위치해야 한다.
def cond(k):
    for i in range(k):
        if arr[i]==arr[k] or abs(arr[i]-arr[k])==abs(i-k):
            return False
        
    return True

def dfs(k):
    if(n==k):
        global ans
        ans+=1
        return
    
    for i in range(n):
        arr[k]=i
        if cond(k):
            dfs(k+1)
    
dfs(0)
print(ans)