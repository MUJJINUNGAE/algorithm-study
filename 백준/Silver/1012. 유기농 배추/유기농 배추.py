import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

T = int(input())

def dfs(farm, x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    farm[y][x] = -1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < M and 0 <= ny < N:
            if farm[ny][nx] == 1:
                dfs(farm, nx, ny)
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
                farm = dfs(farm, x, y)
                warm += 1
            
    print(warm)    