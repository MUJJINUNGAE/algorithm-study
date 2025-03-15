import string

alphabet_lower = string.ascii_lowercase
match_alpabet = dict()

for i in range(len(alphabet_lower)):
    match_alpabet[alphabet_lower[i]] = i+1
    
L = int(input())
r = 31
M = 1234567891
a = input()

result = 0
for i in range(len(a)):
    result += match_alpabet[a[i]] * (r**i)
    
print(result%M)