# BOJ - 15683 _ 감시

### [1] 정의
```
브루트포스 DFS

[STATE]
1. IDX 번째까지 CCTV 방향이 정해진 상태 // 필드

[CHOICE]
1. 각 CCTV의 방향

[CONSTRAINT]
1. 방향은 십자형, 네 방향 뿐이다.
2. 벽은 넘어서 볼 수 없다
3. 다른 CCTV는 넘어서 볼 수 있다.

[CHANGE & ROLLBACK]
1. FIELD

[BASE]
1. idx == len(cctv)

[POURING]
1. 현재 필드의 사각 지대가 최소 크기보다 커지면 실패
2. 그럼 변화가 큰 값부터 계산을 하면 가지치기를 빠르게 할 수 있겠다.
3. CCTV 번호가 큰 IDX 부터 계산하자.
```


### [2] 코드
```python
dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

cd = [
    0,
    [[0], [1], [2], [3]],
    [(0, 1), (2, 3)],
    [(0, 3), (3, 1), (1, 2), (0, 2)],
    [(0, 2, 3), (0, 3, 1), (3, 1, 2), (1, 2, 0)],
    [(0, 1, 2, 3)]
]

def dfs(idx, count):
    global cctv, max_checked, field
    
    # [BASE]
    # 끝까지 다 돌아보면 종료 및 감시구역 크기 갱신
    if idx == len(cctv):
        max_checked = max(max_checked, count)
        return
    
    # CHOICE & CONSTRAINT
    # 좌표와 CCTV 번호
    r, c, v = cctv[idx]
    
    for i in cd[v]:
        candidates = set()  # 백트래킹을 위한 집합
        for j in i:
            dr, dc = dirs[j]
            nr, nc = r+dr, c+dc

            # 필드를 나가거나 벽을 만나는 게 아니면 끝까지 간다
            while 0 <= nr < N and 0 <= nc < M and field[nr][nc] != 6:
                if field[nr][nc] == 0:  # 감시되고 있지 않은 빈 공간이면
                    candidates.add((nr, nc))  # 집합에 추가
                    field[nr][nc] = 7  # 필드에 표시
                nr, nc = nr+dr, nc+dc  # 진행
            
        dfs(idx+1, count+len(candidates))  # 재귀

        for a, b in candidates:  # 필드 백트래킹
            field[a][b] = 0


N, M = map(int, input().split())
field = []
cctv = []
zero_count = 0
for r in range(N):
    row = list(map(int, input().split()))
    field.append(row)
    for c in range(M):
        v = row[c]
        if 0 < v < 6:
            cctv.append((r, c, v))
        elif v == 0:
            zero_count += 1 


# 가지치기 위한 방문배열
visited = [[False] * M for _ in range(N)]  # 결국 사용 안함

# 가지치기를 위한 역순 정렬
cctv.sort(key=lambda x: -x[2])

max_checked = float('-inf')
dfs(0, 0)

print(zero_count - max_checked)
```
오랜만에 혼자 힘으로 해결한 문제입니다.  
잘했다고 생각하는 부분은 다음과 같습니다.
1. `가지치기`를 위해 `역순`으로 탐색한 점  
2. cd 리스트의 자료구조를 통일한 점  

가지치기를 깜빡하고 결국 진행하지는 않았지만 아이디어를 떠올린 점이 마음에 듭니다.  
그리고 다른 번호들과 달리 1번 CCTV 의 타입만 달라서 고민을 했었는데 이를 길이가 1인 리스트로 대체해서 코드를 단순화 했습니다.  
1번만 1차원 리스트 순회를 하고 나머지는 2차원 리스트 순회로 코드를 짜다가 영 아닌것 같아서 고민을 했다는 점과 해결책을 찾았다는 점도 만족스럽습니다.

### [3] AI 리팩터링