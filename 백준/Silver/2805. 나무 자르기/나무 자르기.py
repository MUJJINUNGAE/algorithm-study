N, M = map(int, input().split())
tree = list(map(int, input().split()))


def cut_tree(arr, tree_H):
    get_H = 0
    
    for i in range(len(arr)):
        if arr[i] >= tree_H:
            get_H += arr[i] - tree_H

    return get_H


def binary_search(M, tree):
    lo = 0
    hi = max(tree)
    
    while lo + 1 < hi:
        mid = (hi + lo) // 2
        get_H = cut_tree(tree, mid)
        
        if get_H < M:
            hi = mid
        else:
            lo = mid
            
    return lo
          
          
if M == 0:
    print(max(tree))
else:
    print(binary_search(M, tree))