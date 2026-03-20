# BOJ - 5427 불

from collections import deque

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def move(r, c, k, dist):
    global H, W, building

    if k == 1:
        if not (0 <= r < H and 0 <= c < W):
            return False
        
        if building[r][c] == "#":
            return False
        
        if building[r][c] == "*":
            return False

        if dist[r][c]:
            return False

        return True

    else:
        if not (0 <= r < H and 0 <= c < W):
            return 3
        
        if building[r][c] == "#":
            return False

        if building[r][c] == "*":
            return False
    
        if dist[r][c]:
            return False

        return True
    

def escape(pos):
    global fire, building

    q = deque()
    dist = [[False] * W for _ in range(H)]

    for r, c in fire:
        q.append((r, c, 1, 0))
    
    r, c = pos
    dist[r][c] = 0
    q.append((r, c, 2, 0))

    while q:
        r, c, k, d = q.popleft()

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            joudge = move(nr, nc, k, dist)
            if joudge == 3:                
                return d + 1
            elif joudge:
                if k == 1:
                    dist[nr][nc] = True
                    q.append((nr, nc, k, d))
                else:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc, k, d+1))
    
    return "IMPOSSIBLE"


TC = int(input())
for test_case in range(TC):
    W, H = map(int, input().split())
    building = []
    fire = []
    for r in range(H):
        row = input().strip()
        building.append(row)
        for c in range(W):
            if building[r][c] == "*":
                fire.append((r, c))
            if building[r][c] == "@":
                pos = (r, c)
    
    print(escape(pos))