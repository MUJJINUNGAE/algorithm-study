import sys

s = ['[', ']', '(', ')']

while True:
    m = sys.stdin.readline().rstrip()
    if m == '.':
        break
    
    for i in m:
        if i not in s:
            m = m.replace(i, '')
    
    while m:
        if '()' in m:
            m = m.replace('()', '')
        elif '[]' in m:
            m = m.replace('[]', '')
        else:
            break
    
    if m == '':
        print('yes')
    else:
        print('no')