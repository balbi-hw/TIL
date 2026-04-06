

from collections import deque

def proceed_calculation(cur_num: int) -> list[int]:
    return [cur_num + 1, cur_num - 1, cur_num * 2, cur_num - 10]


def bfs(START: int, END: int) -> None:
    global MAX

    count = 0
    dq = deque()
    dq.append((START, count))

    visited = {START}

    while dq:
        num, cur_cnt = dq.popleft()

        if num == END:
            return cur_cnt
        
        next_numbers = proceed_calculation(num)

        for number in next_numbers:
            if number <= 0:
                continue

            if num > 10**6:
                continue

            if number not in visited:
                visited.add(number)
                dq.append((number, cur_cnt + 1))


TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    MAX = float('inf')
    
    print(f"#{test_case} {bfs(N, M)}")