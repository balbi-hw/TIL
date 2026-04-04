"""
대놓고 백트래킹 문제

밖으로 나갈 수 없게 padding 하고 각 선로 별 분기처리 하면 되겠다.

1. 패딩
2. 선로 분기처리
    - 설치하려는 선로의 다음 방향에 이어질 수 있는 선로가 와야한다.
    - 탈주범 검거 파이프
3. 백트래킹

격자가 주어지니까 패딩을 
N = len(grid)
열 먼저 하는 게 편하겠다
for r in range(N):
    grid[r] = [-1] + grid[r]
    grid[r] += [-1]

grid = [-1]*(N+2) + grid + [-1]*(N+2)
"""
import sys
sys.setrecursionlimit(10**7)

def solution(grid):
    answer = 0
    
    # ===== #
    N = len(grid)
    for r in range(N):
        grid[r] = [-1] + grid[r]
        grid[r] += [-1]
    
    # 격자 완성
    grid = [[-1] * (N + 2)] + grid + [[-1] * (N + 2)]
    
    # 방문 기록
    visited = [[False] * (N + 2) for _ in range(N + 2)]
    
    # 방향
    dirs =[
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]
    
    rail = [
        [0],
        [2, 3],
        [0, 1],
        [0, 1, 2, 3],
        [1, 3],
        [1, 2],
        [0, 2],
        [0, 3]
    ]
    
    # 선로 연결 확인
    oppo = [
        1, 0, 3, 2
    ]
    
    # 가지 수
    count = 0
    # candidate_grid = []
    
    # 백트래킹 함수
    def set_rail(
        r: int, c: int,
        er: int, ec: int,
        grid: list, visited: list
    ) -> None:
        nonlocal count
        
        N = len(grid)
        M = len(grid[0])
        
        # BaseCase: 중간 지점
        if (r, c) == (er, ec):
            candidate_grid.append(grid)
            return
        
        # BaseCase2: 최종 목표
        if (r, c) == (N-1, M-1):
            count += 1
            return
    
        # pouring
        # 가지치기 불가?
        # 3번 레일일 때 조건 확인
        if grid[r][c] == 3:
            for dr, dc in dirs:
                nr, nc = r + nr, c + dc
                if grid[nr][nc] == -1:
                    return
        
        # BackTracking
        for i in rail[grid[r][c]]:
            dr, dc = dirs[i]
            nr, nc = r + dr, c + dc
            
            # 장애물, 패딩은 안간다.
            if grid[nr][nc] == -1:
                continue
                
            # 이미 선로가 있는 곳일 때
            if grid[nr][nc] != 0:
                visited[nr][nc] = True
            
                set_rail(nr, nc, grid, visited)
            
                visited[nr][nc] = False
            
            # 방문한 곳인데 선로가 3번 선로라면 진행
            # 3번 선로 상태를 유지해야겠다
            if visited[nr][nc]:
                if grid[nr][nc] == 3:
                    pass
                else:
                    continue
                    
            
            # 새 좌표에 대해 모든 선로를 다 깔아본다.
            # nrail 번호에 따른 분기처리를 하긴 해야겠다.
            # 3번을 제외하면 들어가는 방향을 리스트에서 뺀 게 다음 방향이니까
            # 해당 방향의 앞에 장애물이 있으면.. 이거 그냥 다음 재귀에서 처리되니까 따로 하지 말자
            # 그럼 3번만 체크
            # 1. 우선 가장자리에는 3번이 들어갈 수 없다.
            #   - 
            for nrail in range(1, 8):
                
                # if nrail == 3:
                    
                
                # 연결이 안되어 있으면 패스
                if oppo[i] not in rail[nrail]:
                    continue
                
                visited[nr][nc] = True
                grid[nr][nc] = nrail
                
                set_rail(nr, nc, grid, visited)
                
                visited[nr][nc] = False
                grid[nr][nc] = 0
    
    set_rail(1, 1, grid, visited)
    answer = count
    
    # ===== #
    
    return answer