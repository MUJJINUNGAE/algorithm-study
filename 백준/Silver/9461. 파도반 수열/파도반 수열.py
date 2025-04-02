T = int(input())

dp = [0, 1, 1, 1, 2, 2]

for _ in range(T):
    N = int(input())
    
    if N > 5:
        dp = dp + [0] * (N-5)
        for i in range(6, N+1):
            dp[i] = dp[i-1] + dp[i-5]
            
    print(dp[N]) 