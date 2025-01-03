num = [int(input()) for _ in range(3)]
    
for i in range(10):
    print(str(num[0] * num[1] * num[2]).count(str(i)))
