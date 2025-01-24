import sys
input = sys.stdin.readline

while (num := input().strip()) != '0':
    print('yes' if num == num[::-1] else 'no')