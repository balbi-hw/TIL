# BOJ - 17471  게리맨더링

from itertools import combinations

N = int(input())
popularity = [0] + list(map(int, input().split()))
info = [[] for _ in range(N+1)]
for i in range(1, N+1):
    status = list(map(int, input().split()))
    info[i] = status[1:]

def dfs(idx: int, visited: list) -> None:
    global info, area_b, area_a

    for num in info[idx]:
        if (idx in area_a and num in area_a) or (idx in area_b and num in area_b):
            if not visited[num]:
                visited[num] = True
                dfs(num, visited)

    pass

def check() -> bool:

    count = 0
    visited = [False] * (N + 1)
    for idx in range(1, N+1):
        if not visited[idx]:
            count += 1
            visited[idx] = True
            dfs(idx, visited)

    return True if count == 2 else False



min_dif = 100*10

for j in range(1, N//2+1):
    sectors = combinations(range(1, N+1), j)
    for sector in sectors:
        area_a = sector
        area_b = []
        for i in list(range(1, N+1)):
            if i not in area_a:
                area_b.append(i)

        if check():
            popularity_a = 0
            popularity_b = 0
        
            for i in area_a:
                popularity_a += popularity[i]
            
            for j in area_b:
                popularity_b += popularity[j]
            
            dif = abs(popularity_a - popularity_b)
            min_dif = min(min_dif, dif)
    
print(min_dif if min_dif != 100*10 else -1)