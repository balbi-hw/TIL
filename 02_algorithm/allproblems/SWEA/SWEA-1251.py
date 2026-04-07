# SWEA - 1251 | 하나로
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15StKqAQkCFAYD&categoryId=AV15StKqAQkCFAYD&categoryType=CODE&problemTitle=1251&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&


def check_island() -> list:

    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    islands = [(x_list[i], y_list[i]) for i in range(N)]

    return islands


def make_info(islands: list) -> list:

    info = []
    # info = [0] * (N - 1)
    tax_rate = float(input())

    for i in range(N - 1):
        ix, iy = islands[i]
        for j in range(i + 1, N):
            jx, jy = islands[j]

            cost = tax_rate * abs((ix - jx)**2 + (iy - jy)**2)
            # info[i] = (j, cost)
            info.append((i, j, cost))
    
    return info


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):

    root_x = find_set(x)
    root_y = find_set(y)

    if root_y != root_x:
        parent[root_y] = parent[root_x]
        return True
    return False


TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())

    islands = check_island()
    info = make_info(islands)
    info.sort(key=lambda x: x[2])

    parent = list(range(N + 1))
    
    total_cost = 0
    count = 0

    # for i in range(N - 1):
    #     j, cost = info[i]
    for i, j, cost in info:

        if union(i, j):
            total_cost += cost
            count += 1
        
            if count == N:
                break
    
    print(f"#{test_case} {round(total_cost)}")