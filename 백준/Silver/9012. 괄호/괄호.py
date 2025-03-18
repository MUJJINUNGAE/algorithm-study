T = int(input())
PS = [input() for _ in range(T)]

for s in PS: 
  while True:
      if '()' in s:
          s = s.replace('()', '')
      else:
          break
      
  if s == '':
      print('YES')
  else:
      print('NO')