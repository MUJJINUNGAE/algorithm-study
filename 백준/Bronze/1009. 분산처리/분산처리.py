T = int(input())

two = [2, 4, 8, 6]
three = [3, 9, 7, 1]
four = [4, 6]
seven = [7, 9, 3, 1]
eight = [8, 4, 2, 6]
nine = [9, 1]

for _ in range(T):
    a, b = map(int, input().split())
    a = int(str(a)[-1])
    if a % 10 == 0:
        print(10)
    elif a == 2:
        print(two[b%4-1])
    elif a == 3:
        print(three[b%4-1])
    elif a == 4:
        print(four[b%2-1])
    elif a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif a == 7:
        print(seven[b%4-1])
    elif a == 8:
        print(eight[b%4-1])
    elif a == 9:
        print(nine[b%2-1])
    else:
      print(1)