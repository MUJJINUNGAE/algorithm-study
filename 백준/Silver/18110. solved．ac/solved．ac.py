import sys

input = sys.stdin.readline

n = int(input())

def custom_round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

if n == 0:
    print(0)
else:
    difficulty = [int(input()) for _ in range(n)]
    difficulty.sort()
    cut = custom_round(len(difficulty) * 0.15)
    difficulty_cut = difficulty[cut:len(difficulty) - cut]
    result = custom_round(sum(difficulty_cut) / len(difficulty_cut))
    print(result)