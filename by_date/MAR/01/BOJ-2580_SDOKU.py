# BOJ - 2580
# 스도쿠

import copy

N = 9

lst = []  # 0 좌표 리스트
board = []
for r in range(9):
    row = list(map(int, input().split()))
    for c in range(9):
        if row[c] == 0:
            lst.append((r, c))
    board.append(row)

# print(lst)
# print(board)
# 좌표마다 후보군 리스트 생성하고
# 확정되고 사용되면 전체에서 지운다


# 1. 해당 0 좌표에 들어갈 수 있는 후보 정리
# 2. 후보가 한 개인 좌표부터 채워나간다.

# 1-1. 함수를 만들어서 사전형에 넣어보자.
cand_info = {}

def cand(r, c):
    global cand_info
    # 가로
    rv = [False] * (N+1)
    for num in board[r]:
        rv[num] = True
    for idx in range(N+1):
        if rv[idx] == False:
            if (r, c) not in cand_info:
                cand_info[(r, c)] = set()
                cand_info[(r, c)].add(idx)
            else:
                cand_info[(r, c)].add(idx)

    # 세로
    cv = [False] * (N+1)
    for row in range(N):
        cv[board[row][c]] = True
    for idx in range(N+1):
        if cv[idx] == False:
            if (r, c) not in cand_info:
                cand_info[(r, c)] = set()
                cand_info[(r, c)].add(idx)
            else:
                cand_info[(r, c)].add(idx)
        
    pass

for r, c in lst:
    cand(r, c)  # 후보군 생성


# 구역 판별도 해야하는데 그냥 dfs 로 밀어붙여볼까

def dfs(board):
    global lst, cand_info

    # 기저조건
    # 조건 만족 못하면 종료

    # 반복
    # 하나 선택 후 다음 인덱스로
    for r, c in lst:
        for num in cand_info[(r, c)]:
            nboard = copy.deepcopy(board)
            board[r][c] = num

            dfs(board)

            board = copy.deepcopy(nboard)

    pass