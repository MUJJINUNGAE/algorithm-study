from collections import deque

card = deque([i+1 for i in range(int(input()))])

while len(card) > 1:
    card.popleft()
    card.rotate(-1)
    
print(*card)