T = int(input())
num = [int(input()) for _ in range(T)]
m = max(num)
dp = [[0, 0] for _ in range(m+1)]
dp[0][0] = 1

for i in range(m+1):
    if i == 0:
        pass
    elif i == 1:
        dp[1][1] = 1
    else:
        dp[i][0] = dp[i-2][0] + dp[i-2][1]
        dp[i][1] = dp[i-1][0] + dp[i-1][1]
        
for j in num:
    print(*dp[j])