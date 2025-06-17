import sys

n, c = map(int,sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()

l=0 # 공유기 사이 거리 최소값
r=arr[-1]-arr[0] # 공유기 사이 거리 최대값
ans=0 # 인접한 공유기 사이 최대 거리

while l<=r:
    m=(l+r)//2 # 공유기 간 최대 거리 후보값
    
    # 첫 번째 집에는 공유기를 반드시 설치한다.
    prev=arr[0] # 직전에 공유기를 설치한 잡
    cnt=1 # 설치한 공유기의 수
    for i in range(1, n):
        if arr[i]-prev>=m:
            cnt+=1
            prev=arr[i]

    if cnt>=c:
        ans=m
        l=m+1
    else:
        r=m-1

print(ans)