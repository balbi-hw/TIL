# BOJ - 2042 - 구간 합 구하기
# 세그먼트 트리 연습 문제

# 그냥 박고 시작하자. 안쓰니까 시간초과 거의 확정이네
import sys
input = sys.stdin.readline

'''
세그먼트 트리 구현 문제
'''

def change(idx: int, value: int):
    global seg, size

    idx += size
    seg[idx] = value

    # idx 의 부모 노드는 idx//2
    node = idx // 2

    # 이걸 루트노드까지 가야함
    while node > 0:
        seg[node] = seg[2*node] + seg[2*node + 1]
        node //= 2


def make_total(start: int, end: int):
    global seg

    '''
    size + idx 가 시작해야하는 리프노드가 된다.
    range(size + start, size + end)
    '''
    start += size
    end += size
    result = 0

    while start <= end:
        if start % 2 == 1:
            result += seg[start]
            start += 1
        
        if end % 2 == 0:
            result += seg[end]
            end -= 1
        
        start //= 2
        end //= 2

    return result


N, M, K = map(int, input().split())
nums = [int(input().strip()) for _ in range(N)]


# --- 트리 구현 --- #
size = 1
while size < N:
    size *= 2

seg = [0] * (2 * size)

# 리프노드 채우고
for i in range(N):
    seg[size+i] = nums[i]

# 자식노드의 합으로 부모노드 채우기
for i in range(size-1, 0, -1):
    seg[i] = seg[2*i] + seg[2*i+1]
# ---------------- #
    

for _ in range(M+K):
    order, B, C = map(int, input().split())
    B -= 1

    # pre_val = []  백트래킹 필요 없다.
    if order == 1:
        # pre_val.append((B, nums[B]))
        change(B, C)

    else:
        C -= 1
        print(make_total(B, C))

'''
[*] 중요한 관찰 [*]

각 레벨에서

왼쪽 경계
오른쪽 경계

딱 두 개의 포인터만 존재한다.

l ----------- r

이 두 포인터 사이의 노드들은 이미 부모 노드로 합쳐진 상태.
=> 독립된 노드만 확인하면 되고 이 독립 여부를 판단하는게

l % 2 == 1 ?
r % 2 == 0 ?

l % 2 == 1 이면 l 포인터가 오른쪽 자식이라는 뜻이고 고립되었다는 뜻
r % 2 == 0 이면 r 포인터가 왼쪽 자식이고 고립되었다는 뜻
'''