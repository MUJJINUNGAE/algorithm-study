N = int(input())

def makeone(n):
    if n < 3:
        return n-1
    else:
        return 1 + min(makeone(n//2) + n%2, makeone(n//3) + n%3)
        
print(makeone(N))