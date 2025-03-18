N = int(input())
step = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)

for i in range(1, N+1):
    if N == 1:
        dp[1] = step[1]
    elif N == 2:
        dp[2] = step[1] + step[2]
    else:
        dp[i] = dp[i-2] + step[i]
        dp[i] = max(dp[i], dp[i-3] + step[i-1] + step[i])

print(dp[N])