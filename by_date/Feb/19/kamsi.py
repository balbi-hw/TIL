# BOJ - 15683
# 감시

from collections import deque

# CCTV 는 회전이 가능하다.
# 5번은 전방향이 가능하니 회전 의미 없고
# 벽을 뚫지 못한다.
# 사각지대 최소크기
# DFS?
# 모든 경우의 수 판단


# 상태변수는
# 방향? for문 if문 조합하면 될지도?

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

rotate = {
    1: dirs,
    2: [(0, 1), (2, 3)],
    3: [(0, 3), (3, 1), (1, 2), (0, 2)],
    4: dirs
}

N, M = map(int, input().split())

field = []
cctv = [[] for _ in range(6)]
cctv_num = 0
for r in range(N):
    field.append(list(map(int, input().split())))
    for c in range(M):
        if 0 < field[r][c] <= 5:
            cctv[field[r][c]].append((r, c))
            cctv_num += 1
print(cctv)

# 1: 한방향
# 2: 양방향
# 3: 직각 두 방향
# 4: 세 방향
# 전선 까는거랑 비슷한데
# 그리드로 각자 제일 많이 깔면 되잖아?
# 그건 아니네..
# 아니면 그냥 집합으로?
# 집합하면 중복도 신경 안써도 되고
# 백트래킹도 필요 없는거 아닐까

def dfs(idx, area):
    global field, cctv_num, N, M
    # 하나하나 확인하며 그녀석이 쓸 수 있는 모든 방향 확인하기

    # 종료조건
    # idx 끝
    if idx == cctv_num:





    pass