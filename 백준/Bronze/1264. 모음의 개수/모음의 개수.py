vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    s = input()
    
    if s == '#':
        break
    
    cnt = 0
        
    for i in s:
        if i in vowel:
            cnt += 1
            
    print(cnt)