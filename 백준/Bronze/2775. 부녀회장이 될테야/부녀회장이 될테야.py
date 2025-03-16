T = int(input())
floor = []

for i in range(T):
    floor = []
    k = int(input())
    n = int(input())
    
    floor.append([i for i in range(1, n+1)])
    
    for j in range(k):
        floor.append([sum(floor[j][:a]) for a in range(1,n+1)])
        
    print(floor[k][n-1])