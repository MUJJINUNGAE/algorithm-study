import sys
input = sys.stdin.readline


def check(p):
    first_value = p[0][0]
    
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i][j] != first_value:
                return False
    return str(first_value)
    
    
def cut(paper):
    chk = check(paper)
    if chk:
        return chk
        
    n = len(paper) // 2

    return (
        cut([x[:n] for x in paper[:n]]) +
        cut([x[n:] for x in paper[:n]]) +
        cut([x[:n] for x in paper[n:]]) +
        cut([x[n:] for x in paper[n:]])
        )
        
        
size = int(input())
paper = [list(map(int, input().split())) for _ in range(size)]
cut_paper = cut(paper)

print(cut_paper.count('0'))
print(cut_paper.count('1'))