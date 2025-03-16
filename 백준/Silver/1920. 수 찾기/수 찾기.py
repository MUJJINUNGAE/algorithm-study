N = int(input())
A = {i:1 for i in list(input().split())}
M = int(input())
num = list(input().split())

for j in num:
    try:
        print(A[j])
    except:
        print(0)