i = 3

for _ in range(3):
    a = input()
    try:
        a = int(a)
        b = a + i
        i -= 1
    except:
        i -= 1
  
if b%3 == 0 and b%5 == 0:
    print('FizzBuzz')
elif b%3 == 0:
    print('Fizz')
elif b%5 == 0:
    print('Buzz')
else:
    print(b)