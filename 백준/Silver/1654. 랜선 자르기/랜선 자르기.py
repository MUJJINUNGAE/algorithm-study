import sys

input = sys.stdin.readline

K, N = map(int, input().split())
rope = [int(input()) for _ in range(K)]

def num_rope(arr, length):
    num = 0
    
    for i in range(K):
        num += arr[i] // length
     
    return num


def upper_bound(arr, hi, lo, N):
    while lo + 1 < hi:
        mid = (hi + lo) // 2
        
        if num_rope(arr, mid) >= N:
            lo = mid
        else:
            hi = mid

    return lo
    
    
if K == N and min(rope) == max(rope):
    print(min(rope))
else:
    answer = upper_bound(rope, max(rope), 1, N)
    print(answer)