import math

n = int(input())

def four_square(n):
    square = int(math.sqrt(n))
    
    if square == math.sqrt(n):
        return 1
    
    for i in range(1, square + 1):
        if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
            return 2
            
    for i in range(1, square + 1):
        for j in range(1, int(math.sqrt(n - i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                return 3
                
    return 4
    
print(four_square(n))