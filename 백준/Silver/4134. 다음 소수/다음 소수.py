T = int(input())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

for _ in range(T):
    n = int(input())
    prime = is_prime(n)
    
    while not prime:
        n += 1
        prime = is_prime(n)
        
    print(n)