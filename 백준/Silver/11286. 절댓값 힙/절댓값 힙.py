import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    n = int(input())
    if n == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(n), n))