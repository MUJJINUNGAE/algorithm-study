import sys

input = sys.stdin.readline
N, K = map(int, input().strip().split(' '))
coinlist = [int(input().strip()) for _ in range(N)]
i = 0

for coin in reversed(coinlist):
    i += K // coin
    K %= coin
        
print(i)