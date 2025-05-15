import sys

input = sys.stdin.readline


def check(p):
    first_value = p[0][0]
    
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i][j] != first_value:
                return False
    if first_value == 1:
        return '1'
    else:
        return '0'
    
    
def cut(paper):
    n = len(paper) // 2
    chk = check(paper)
    
    if chk:
        return chk
    
    else:
        paper1 = [x[:n] for x in paper[:n]]
        paper2 = [x[n:] for x in paper[:n]]
        paper3 = [x[:n] for x in paper[n:]]
        paper4 = [x[n:] for x in paper[n:]]
        
        return cut(paper1) + cut(paper2) + cut(paper3) + cut(paper4)
        
        
size = int(input())
paper = []

for _ in range(size):
    paper.append(list(map(int, input().split())))

    
cut_paper = cut(paper)
cnt_one = 0

for i in cut_paper:
    if i == '1':
        cnt_one += 1
        
print(len(cut_paper) - cnt_one)
print(cnt_one)