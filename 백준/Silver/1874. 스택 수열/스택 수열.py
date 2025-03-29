import sys

input = sys.stdin.readline

n = int(input())
stack = []
result = []
current = 1

for _ in range(n):
    i = int(input())
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