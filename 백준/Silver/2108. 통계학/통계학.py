import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
num = sorted([int(input()) for _ in range(N)])
s = sum(num)
l = len(num)

counter = Counter(num)
m = max(counter.values())
mode = []

for i in counter.most_common():
    if i[1] == m:
        mode.append(i[0])
        
print(int(s/l + 0.5) if s >= 0 else -int(abs(s)/l + 0.5))
print(num[int((l/2))])
print(mode[0] if len(mode) == 1 else mode[1])
print(max(num) - min(num))