import math
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
	N, M = map(int, input().strip().split())
	
	print(math.factorial(M) // (math.factorial(M-N) * math.factorial(N)))