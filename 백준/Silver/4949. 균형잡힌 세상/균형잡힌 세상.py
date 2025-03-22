while True:
    temp = []
    m = input()
    if m == '.':
        break
    
    for i in m:
        if i == '[':
            temp.append(i)
        elif i == ']':
            if not temp or temp[-1] != '[':
                temp.append(i)
                break
            else:
                temp.pop()
            
        elif i == '(':
                temp.append(i)
        elif i == ')':
            if not temp or temp[-1] != '(':
                temp.append(i)
                break
            else:
                temp.pop()
        
    if not temp:
        print('yes')
    else:
        print('no')