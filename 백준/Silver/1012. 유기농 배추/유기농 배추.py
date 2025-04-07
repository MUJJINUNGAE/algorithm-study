import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def bfs(farm, x, y):
    queue = deque([[x, y]])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    farm[y][x] = -1
    
    while queue:
        v = queue.popleft()
        
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N:
                if farm[ny][nx] == 1:
                    queue.append([nx, ny])
                    farm[ny][nx] = -1
    return farm
            
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    warm = 0
    
    for x in range(M):
        for y in range(N):
            if farm[y][x] == 1:
                farm = bfs(farm, x, y)
                warm += 1
            
    print(warm)