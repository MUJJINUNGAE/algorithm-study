import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    answer = [pow(a, i, 10) for i in range(1, 5)][b % 4 - 1]
    
    print(answer if answer != 0 else 10)