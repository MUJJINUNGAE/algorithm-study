s = input()

cal = s.split('-')

for i in range(len(cal)):
    if '+' in cal[i]:
        cal[i] = cal[i].split('+')
        cal[i] = sum(map(int, cal[i]))
        
cal = list(map(int, cal))
result = cal[0] - sum(cal[1:])
print(result)