from collections import deque
import sys
sys.setrecursionlimit(10**7)

N, M, V = map(int, input().split())
start = V
G = [[] for _ in range(N+1)]
dfs_root = []
bfs_root = []
dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in G:
    i = i.sort()

def dfs(start, visited):
    global G
    dfs_root.append(start) # dfs_root 재귀마다 기록

    visited[start] = True
    for v in G[start]:
        if not visited[v]:
            dfs(v, visited)
    
    return visited

def bfs(start, visited):
    global G
    
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        bfs_root.append(v) # bfs_root while문 기록

        for i in G[v]:

            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return visited

dfs(V, dfs_visited)
bfs(V, bfs_visited)

print(' '.join([str(i) for i in dfs_root]))
print(' '.join([str(i) for i in bfs_root]))