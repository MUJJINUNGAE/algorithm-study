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
        
if 'NO' in result:
  print('NO')
else:
  for i in result:
      print(i)