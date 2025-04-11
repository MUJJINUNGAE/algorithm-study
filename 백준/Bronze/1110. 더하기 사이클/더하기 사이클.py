N = input()
if int(N) < 10:
    N = '0' + N
stop = N
i = 0

while True:
    a, b = int(str(N)[0]), int(str(N)[1])
    s = a + b
    N = str(N)[-1] + str(s)[-1]
    i += 1
    
    if N == stop:
        break
    
print(i)