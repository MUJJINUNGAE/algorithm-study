a = input().upper()
L = [chr(i) for i in range(65, 91)]
c = []

for i in L:
    c.append(a.count(i))

if c.count(max(c)) == 1:
    print(chr(65 + c.index(max(c))))

else:
    print('?')