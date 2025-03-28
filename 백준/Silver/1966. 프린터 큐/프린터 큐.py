import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    important = list(map(int, input().split()))
    doc = deque([[i, important[i]] for i in range(N)])
    n = 1
    
    while True:
        if N == 1:
            print(n)
            break
            
        else:
            if doc[0][1] < max([x[1] for x in doc]):
                doc.rotate(-1)
                
            else:
                prt = doc.popleft()
                if prt[0] == M:
                    print(n)
                    break
                n += 1