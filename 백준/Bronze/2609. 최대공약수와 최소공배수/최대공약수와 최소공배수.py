A, B = map(int, input().split())

[a, b] = [max(A, B), min(A, B)]

while b != 0:
	[a, b] = [b, a % b]
	
print(f'{a}')
print(f'{(A//a) * (B//a) * a}')