def assign_room(T, data):
    result = []
    for i in range(T):
        H, W, N = data[i]
        
        floor = N % H if N % H != 0 else H
        room = (N - 1) // H + 1
        
        result.append(f"{floor}{room:02d}")
    
    return result

T = int(input())  
data = [tuple(map(int, input().split())) for _ in range(T)]

result = assign_room(T, data)
for res in result:
    print(res)
