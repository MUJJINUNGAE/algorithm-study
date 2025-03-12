def fibonacci(n):
    a, b = 1, 0
    if n == 0:
        return a, b
    elif n == 1:
        return b, a
    else:
        temp = fibonacci(n-2)
        a = sum(temp)
        b = a + temp[1]
        return a, b

T = int(input())

for _ in range(T):
    print(*fibonacci(int(input())))