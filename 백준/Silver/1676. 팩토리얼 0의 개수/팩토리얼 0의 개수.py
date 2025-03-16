N = int(input())
f = 1
count = 0

for i in range(1, N+1):
    f *= i
    
for num in str(f)[::-1]:
    if num == '0':
        count += 1
    else:
        break
    
print(count)