# 목차
- [목차](#목차)
  - [문제 정리](#문제-정리)
  - [후기](#후기)
  - [코드](#코드)
    - [1. 브루트 포스](#1-브루트-포스)
    - [2. 수학](#2-수학)
    - [3. 해설 코드](#3-해설-코드)



## 문제 정리

- **문제명 / 번호**:  
  BOJ - 3197 | 백조의 호수

- **유형**:  
  BFS

- **핵심 키워드**:  
  필드의 변경 및 글로벌 큐 관리

- **상태 정의**:  
  현재 필드 상태

- **핵심 아이디어**:  
  큐를 글로벌로 관리한다는 점이 핵심인 문제

- **시간복잡도**:  
  O(N*M)

  
## 후기

브루트포스로 구현에는 성공했지만 최적화에 실패했습니다. 큐는 로컬에서만 관리한다는 감각이 있어서 BFS 를 돌릴 때마다 새 큐를 만들고 진행하고 만들고 진행하고 하다보니 시간 복잡도가 터지고 시간 복잡도를 해결하면 메모리가 터져버렸습니다.  
  
큐를 글로벌로 관리한다는 개념이 없었는데 이 문제의 해설 코드를 찾으며 알게 되었습니다. 해결에 실패해서 기분이 좋지는 않지만 결국 피와 살이 될 것이라고 믿습니다.
  
아래는 코드입니다.

## 코드

### 1. 브루트 포스
```python
# BOJ - 3197 | 백조의 호수
# https://www.acmicpc.net/problem/3197

import sys
from collections import deque

input = sys.stdin.readline

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


def is_done(swans: list) -> bool:

    r, c = swans[0]
    er, ec = swans[1]

    q = deque()
    q.append((r, c))
    visited = [[False] * C for _ in range(R)]
    visited[r][c] = True

    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < R and 0 <= nc < C):
                continue

            if visited[nr][nc]:
                continue

            if lake[nr][nc] == 'L':
                return True

            if lake[nr][nc] != 'X':
                visited[nr][nc] = True
                q.append((nr, nc))

    return False


def swan_area_check(swans: list) -> set:

    q = deque()
    water = set()

    for swan in swans:
        r, c = swan

        q.append((r, c))
        water.add((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < R and 0 <= nc < C):
                    continue

                if (nr, nc) in water:
                    continue

                if lake[nr][nc] == '.':
                    water.add((nr, nc))
                    q.append((nr, nc))

    return water


def melting(water_area: set) -> set:
    
    melted = set()

    for r, c in water_area:
        for dr, dc in dirs:
            nr, nc = r + dr , c + dc

            if not (0 <= nr < R and 0 <= nc < C):
                continue

            if lake[nr][nc] == 'X':
                lake[nr][nc] = '.'
                melted.add((nr, nc))

    return melted


R, C = map(int, input().split())
lake = []
swans = []
for r in range(R):
    row = input().strip()
    lake.append(list(row))
    if 'L' in row:
        swans.append((r, row.index('L')))


days = 0
water_area = swan_area_check(swans)
while not is_done(swans):
    nxt_area = melting(water_area)

    days += 1
    water_area = nxt_area

print(days)
```

### 2. 수학
```python
# BOJ - 3197 | 백조의 호수
# https://www.acmicpc.net/problem/3197

import sys
from collections import deque

input = sys.stdin.readline

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def is_done(swans: list) -> None:

    r, c = swans[0]
    er, ec = swans[1]
    q = deque()
    q.append((r, c, 0))
    dist = [[INF] * C for _ in range(R)]
    dist[r][c] = 0

    while q:
        r, c, count = q.popleft()

        if (r, c) == (er, ec):
            dist[r][c] = min(dist[r][c], count)
            continue

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < R and 0 <= nc < C):
                continue
            
            if dist[nr][nc] > dist[r][c]:
                if lake[nr][nc] == 'X':
                    dist[nr][nc] = count + 1
                    q.append((nr, nc, count + 1))
                else:
                    dist[nr][nc] = count
                    q.append((nr, nc, count))

    return dist[er][ec]


R, C = map(int, input().split())
lake = []
swans = []
for r in range(R):
    row = input().strip()
    lake.append(list(row))
    if 'L' in row:
        swans.append((r, row.index('L')))

INF = 10**18
result = is_done(swans)

if result % 2:
    result //= 2
    result += 1
else:
    result //= 2

print(result)
```

### 3. 해설 코드
```python
# BOJ - 3197 | 백조의 호수
# https://www.acmicpc.net/problem/3197


import sys
from collections import deque

input = sys.stdin.readline

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

R, C = map(int, input().split())
lake = []
swans = []

water_q = deque()

for r in range(R):
    row = list(input().strip())
    for c in range(C):
        if row[c] != 'X':          # 물(.)과 백조(L)는 모두 물 취급
            water_q.append((r, c))
        if row[c] == 'L':
            swans.append((r, c))
    lake.append(row)

(sr, sc), (er, ec) = swans

# 백조 이동용 큐
swan_q = deque([(sr, sc)])
next_swan_q = deque()
swan_visited = [[False] * C for _ in range(R)]
swan_visited[sr][sc] = True


def move_swan() -> bool:
    while swan_q:
        r, c = swan_q.popleft()

        if (r, c) == (er, ec):
            return True

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if swan_visited[nr][nc]:
                continue

            swan_visited[nr][nc] = True

            if lake[nr][nc] == 'X':
                next_swan_q.append((nr, nc))   # 오늘은 못 감, 내일 시도
            else:
                swan_q.append((nr, nc))        # 오늘 바로 이동 가능

    return False


def melt():
    water_size = len(water_q)

    for _ in range(water_size):
        r, c = water_q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < R and 0 <= nc < C):
                continue

            if lake[nr][nc] == 'X':
                lake[nr][nc] = '.'
                water_q.append((nr, nc))


days = 0

while True:
    if move_swan():
        print(days)
        break

    melt()
    swan_q = next_swan_q
    next_swan_q = deque()
    days += 1
```