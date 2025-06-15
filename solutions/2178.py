from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [list(input()) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[0] * m for _ in range(n)] 

visited[0][0] = 1
queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny]=='1':
            visited[nx][ny]+=visited[x][y]+1
            queue.append((nx, ny))

print(visited[-1][-1])