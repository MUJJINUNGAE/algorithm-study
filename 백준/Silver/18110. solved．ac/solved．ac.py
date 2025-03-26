import sys

input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    difficulty = [int(input()) for _ in range(n)]
    difficulty.sort()
    cut = int(len(difficulty) * 0.15 + 0.5)
    difficulty_cut = difficulty[cut:len(difficulty) - cut]
    result = int((sum(difficulty_cut) / len(difficulty_cut) + 0.5))
    print(result)