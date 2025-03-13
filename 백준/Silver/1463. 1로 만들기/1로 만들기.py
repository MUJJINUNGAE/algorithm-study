N = int(input())

# Recursion
def makeone(n):
    if n < 3:
        return n-1
    else:
        return 1 + min(makeone(n//2) + n%2, makeone(n//3) + n%3)
        
print(makeone(N))

# DP
'''
dp = [0] * (N + 1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 6 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1, dp[i//3] + 1)
    elif i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
        
print(dp[N])
'''