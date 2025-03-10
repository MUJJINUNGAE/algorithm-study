import sys

input = sys.stdin.readline
N, K = map(int, input().strip().split(' '))
coinlist = [int(input().strip()) for _ in range(N)]
i = 0

while K != 0:
    coin = coinlist.pop()
    num = K // coin
    if num != 0:
        K %= coin
        i += num
        
print(i)