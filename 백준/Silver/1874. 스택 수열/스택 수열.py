import sys

input = sys.stdin.readline

n = int(input())
seq = [i for i in range(n, 0, -1)]
stack = []
result = []

for i in range(n):
    p = int(input())
    
    if p in seq or p in stack:
        if not stack:
            if i == 0:
                for _ in range(p):
                    stack.append(seq.pop())
                    result.append('+')
                stack.pop()
                result.append('-')
            else:
                while True:
                    s = seq.pop()
                    stack.append(s)
                    result.append('+')
                    
                    if stack[-1] == p:
                        stack.pop()
                        result.append('-')
                        break
        else:
            if stack[-1] >= p:
                while True:
                    if stack.pop() != p:
                        result.append('-')
                    else:
                        result.append('-')
                        break
            
            else:
                while True:
                    s = seq.pop()
                    if s != p:
                        stack.append(s)
                        result.append('+')
                    else:
                        result.append('+')
                        result.append('-')
                        break
            
    else:
        result.append('NO')
        break
    
if 'NO' in result:
    print('NO')
else:
    for i in result:
        print(i)