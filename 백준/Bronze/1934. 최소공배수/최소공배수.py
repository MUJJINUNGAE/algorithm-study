import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
	A, B = map(int, input().split())
	
	[a, b] = [max(A, B), min(A, B)]

	while b != 0:
		[a, b] = [b, a % b]
		
	print((A // a) * (B // a) * a)