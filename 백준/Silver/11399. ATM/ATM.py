N = int(input())
P = sorted(list(map(int, input().split())))
t, w = 0, 0

for i in P:
    t += i
    w += t
    
print(w)