N = int(input())
word = []

for _ in range(N):
    word.append(input())
    
word = list(set(word))

word_sort = sorted(word, key = lambda x:(len(x), x))

for i in word_sort:
    print(i)