case = int(input())

for _ in range(case):
    score = 0
    n = 1
    
    for i in input():
        if i == 'O':
            score += n
            n += 1
        else:
            n = 1
            
    print(score)