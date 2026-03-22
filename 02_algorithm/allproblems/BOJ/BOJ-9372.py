# BOJ - 9372 상근이의 여행
# MST 연습 문제

def make_set(x):
    parent[x] = x

def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px == py:
        return False

    if px < py:
        parent[py] = px
    else:
        parent[px] = py

    return True


TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    parent = list(range(N + 1))
    # 2차원 리스트

    count = 0
    for i in range(M):
        p, c = map(int, input().split())
        if union(p, c):
            count += 1
    
    print(count)

#####
'''
정답.

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    for _ in range(M):
        input()
    print(N - 1)
'''