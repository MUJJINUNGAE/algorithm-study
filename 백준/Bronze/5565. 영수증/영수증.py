total = int(input())
check_price = 0

for i in range(9):
    check_price += int(input())
    
print(total - check_price)