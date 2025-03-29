import sys

input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]
stack = []
result = []
current = 1

for i in seq:
    while current <= i:
        stack.append(current)
        result.append('+')
        current += 1
    
    if stack and stack[-1] == i:
        stack.pop()
        result.append('-')
    else:
        result = ['NO']
        break

for i in result:
    print(i)  