num = list(map(int, input().split()))
a = 0

for i in num:
    a += i ** 2

print(a % 10)