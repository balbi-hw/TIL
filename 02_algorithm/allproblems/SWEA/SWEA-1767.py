# SWEA - 1767 | 프로세서 연결하기

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


def checking(r, c, d):
    dr, dc = dirs[d]
    nr, nc = r + dr, c + dc
    
    wired = []
    while (0 <= nr < N and 0 <= nc < N):
        if field[nr][nc] == 1:
            return []
        if checked[nr][nc]:
            return []
        

        wired.append((nr, nc))

        nr, nc = nr + dr, nc + dc
    
    return wired


def dfs(idx: int, val: int, connected: int):
    global MIN, MAX_connected

    
    # pouring
    if connected + quantity - idx < MAX_connected:
        return
    
    # base
    if idx == quantity:
        if connected > MAX_connected:
            MAX_connected = connected
            MIN = val
        elif connected == MAX_connected:
            MIN = min(MIN, val)
        return
    # recur
    r, c = cores[idx]
    for d in range(4):
        wired = checking(r, c, d)
        if not wired:
            continue
        
        for row, col in wired:
            checked[row][col] = True

        dfs(idx + 1, val + len(wired), connected + 1)

        for row, col in wired:
            checked[row][col] = False
    
    dfs(idx + 1, val, connected)


TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    field = []
    cores = []
    for r in range(N):
        row = list(map(int, input().split()))
        field.append(row)
        for c in range(N):
            if row[c] == 1:
                if r not in (0, N - 1) and c not in (0, N - 1):
                    cores.append((r, c))
    quantity = len(cores)

    checked = [[False] * N for _ in range(N)]
    MIN = 10**7
    MAX_connected = 0

    dfs(0, 0, 0)

    print(MIN)