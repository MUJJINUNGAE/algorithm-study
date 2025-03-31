import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
c = int(input())
network = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(c):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            
    return visited
    
virus = bfs(network, 1, visited)
print(sum(virus)-1)