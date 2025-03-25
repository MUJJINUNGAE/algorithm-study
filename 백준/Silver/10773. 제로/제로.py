K = int(input())
book = []

for _ in range(K):
    money = int(input())
    if money == 0:
        book.pop()
    else:
        book.append(money)
        
print(sum(book))