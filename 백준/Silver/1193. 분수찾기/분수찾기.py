X = int(input())

line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    print(f'{X}/{line-X+1}')

else:
    print(f'{line-X+1}/{X}')