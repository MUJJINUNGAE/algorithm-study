import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    cloth_list = {}
    x = []
    for _ in range(n):
        cloth, category = input().split()
        
        if category not in cloth_list:
            cloth_list[category] = [cloth]
        else:
            cloth_list[category].append(cloth)
        
    combi = 1
    
    for i in cloth_list:
        combi *= (len(cloth_list[i]) + 1)
        
    print(combi-1)