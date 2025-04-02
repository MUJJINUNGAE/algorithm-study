T = int(input())

dp = [0, 1, 1, 1, 2, 2]
N = [int(input()) for _ in range(T)]
m = max(N)

if m > 5:
    dp = dp + [0] * (m-5)
    for i in range(6, m+1):
        dp[i] = dp[i-1] + dp[i-5]

for i in N:
    print(dp[i])