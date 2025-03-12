import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
memo = dict()

for _ in range(N):
    cite, pwd = input().strip().split()
    memo[cite] = pwd
    
for _ in range(M):
    cite = input().strip()
    print(memo[cite])