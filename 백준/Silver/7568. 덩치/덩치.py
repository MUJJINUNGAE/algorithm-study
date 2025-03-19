N = int(input())
size = [list(map(int, input().split())) for _ in range(N)]
result = []

for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            pass
        elif size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            rank += 1
    result.append(rank)
            
print(*result)