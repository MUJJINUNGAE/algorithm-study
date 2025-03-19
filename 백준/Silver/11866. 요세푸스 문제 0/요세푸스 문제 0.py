from collections import deque

N, K = map(int, input().split())
pm = deque([i for i in range(1, N+1)])
josephus = []
cnt = 0

while pm:
    if cnt != K-1:
        pm.rotate(-1)
        cnt += 1
    else:
        josephus.append(pm.popleft())
        cnt = 0

print(f'<{", ".join(map(str, josephus))}>')
