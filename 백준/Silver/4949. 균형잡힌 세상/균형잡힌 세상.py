s = ['[', ']', '(', ')']

while True:
    m = input()
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