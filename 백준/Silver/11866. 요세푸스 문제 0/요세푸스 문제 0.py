N, K = map(int, input().split())
pm = [i for i in range(1, N+1)]
josephus = []
idx = 0

while pm:
    idx = (idx + K - 1) % len(pm)
    josephus.append(pm.pop(idx))

print(f'<{", ".join(map(str, josephus))}>')