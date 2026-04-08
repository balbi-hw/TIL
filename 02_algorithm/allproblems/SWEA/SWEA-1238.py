# SWEA - 1238 | Contact
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD


from collections import deque, defaultdict


def make_gragh() -> list[set]:

    gragh = defaultdict(set)
    for i in range(E):
        p, c = info[i*2], info[i*2 + 1]
        gragh[p].add(c)

    return gragh


def get_and_print_last(gragh: dict[set]) -> None:
    N = len(gragh)
    visited = set()

    q = deque([(START, 0)])
    visited.add(START)
    last_num = defaultdict(list)

    while q:
        cur_pos, depth = q.popleft()

        for nxt_pos in list(gragh[cur_pos]):

            if nxt_pos not in visited:
                visited.add(nxt_pos)
                last_num[depth].append(nxt_pos)
                q.append((nxt_pos, depth + 1))

    max_key = max(last_num.keys())
    result = max(last_num[max_key])
    print(f"#{test_case} {result}")


for test_case in range(1, 11):
    E, START = map(int, input().split())
    E //= 2
    info = list(map(int, input().split()))

    gragh = make_gragh()
    get_and_print_last(gragh)