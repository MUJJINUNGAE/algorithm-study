N, K = map(int, input().split())
pm = list(range(1, N+1))
josephus = []
idx = 0

while pm:
    idx = (idx + K - 1) % len(pm)
    josephus.append(str(pm.pop(idx)))

print(f"<{', '.join(josephus)}>")