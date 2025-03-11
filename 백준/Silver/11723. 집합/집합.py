import sys

input = sys.stdin.readline
M = int(input().strip())
S = set()
fullset = set(range(1, 21))

for _ in range(M):
    command = input().strip()
    if command != 'all' and command != 'empty':
        x, y = command.split()
    else:
        x = command
    
    if x == 'add':
        S.add(int(y))
        
    elif x == 'remove':
        S.discard(int(y))
        
    elif x == 'check':
        if int(y) in S:
            print(1)
        else:
            print(0)
        
    elif x == 'toggle':
        try:
            S.remove(int(y))
        except:
            S.add(int(y))
            
            
    elif x == 'all':
        S = fullset.copy()
        
    elif x == 'empty':
        S.clear()