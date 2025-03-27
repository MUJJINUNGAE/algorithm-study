M, N = map(int, input().split())
square = int(N ** 0.5)
prime = [True] * (N - M + 1)

for i in range(2, square + 1):
    start = max(i * i,(M + i - 1) // i * i)
    for j in range(start, N + 1, i):
        if M <= j <= N:
            prime[j - M] = False
 
for i in range(N - M + 1):
    if prime[i] and i + M != 1:
        print(i + M)