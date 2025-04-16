N, M = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

A.symmetric_difference_update(B)

print(len(A))