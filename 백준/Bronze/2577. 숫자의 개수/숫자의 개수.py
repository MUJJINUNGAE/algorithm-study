num = 1

for _ in range(3):
    num = num * int(input())
    
num = str(num)
numbers = [i for i in range(10)]

for i in range(10):
    numbers[i] = num.count(str(numbers[i]))
    
for j in numbers:
    print(j)