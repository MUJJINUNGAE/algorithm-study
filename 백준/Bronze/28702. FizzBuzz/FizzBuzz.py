i = 3
s = []
for _ in range(3):
    a = input()
    try:
        a = int(a)
        x = a + i
        s.append(x)
    except:
        i -= 1

b = s[0]
  
if b%3 == 0 and b%5 == 0:
    print('FizzBuzz')
elif b%3 == 0:
    print('Fizz')
elif b%5 == 0:
    print('Buzz')
else:
    print(b)