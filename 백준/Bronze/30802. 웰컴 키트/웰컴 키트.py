a = int(input())
b = list(map(int, input().split()))
t, p = list(map(int, input().split()))[:]

print(sum([i//t if i%t == 0 else i//t + 1 for i in b]))
print(f'{a//p} {a%p}')