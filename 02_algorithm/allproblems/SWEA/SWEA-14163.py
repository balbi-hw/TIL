# SWEA - 14163  그룹 나누기

def make_set(n):
    return [i for i in range(n+1)]

def find_set(x):
    if x != tree[x]:
        tree[x] = find_set(tree[x])
    return tree[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px < py:
        tree[py] = px
    else:
        tree[px] = py

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))

    tree = make_set(N)
    for i in range(M):
        p, c = info[i*2], info[i*2+1]
        union(p, c)
        
    for i in range(1, N+1):
       tree[i] = find_set(i)
    
    result = set(tree[1:])
    print(f"#{test_case} {len(result)}")
