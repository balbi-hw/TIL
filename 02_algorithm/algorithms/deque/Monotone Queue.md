# 문제 정리

- **문제명 / 번호**:  
  BOJ - 11003 | 최솟값 찾기

- **유형**:  
  슬라이딩 윈도우, Deque

- **핵심 키워드**:  
  deque 를 활용해 슬라이딩 윈도우를 최적화한다.

- **핵심 아이디어**:  
  대상 리스트를 순회하며 deque 에 윈도우 안의 인덱스만 저장한다. 이 때 후보의 가능성이 없어진 인덱스는 바로 제거한다.
  ```python
  for i in range(N):
    while dq and arr[dq[-1]] >= arr[i]:
      dq.pop()
  """
  dq 에 element 가 있을 때, i ( 윈도우 마지막 인덱스 ) 보다 큰 값이 안에 있으면 제거한다. ( 최솟값 가능성을 잃었다. )
  """
  ```

- **시간복잡도**:
  O(N)  
  while 이 있긴 하지만 모든 원소가 한 번 들어가고 한 번 나오기 때문에

- **코드**
```python
# BOJ - 11003 | 최솟값 찾기

from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
numbers = list(map(int, input().split()))

dq = deque()
result = []
for i in range(N):

    # 큐가 활성화 되어 있고 내부에 마지막 인덱스보다 큰 값이 있으면 제거한다.
    while dq and numbers[dq[-1]] >= numbers[i]:
        dq.pop()

    # 현재 인덱스값을 추가한다.
    dq.append(i)

    # 윈도우가 한 번 완성되면 앞에서부터 삭제를 시작한다.
    if dq[0] <= i - L:
        dq.popleft()

    # 현재 인덱스에서 최소값 result 에 추가
    # print(numbers[dq[0]], end=" ") 로 한 번에 출력 할 수도 있음
    result.append(numbers[dq[0]])

print(*result)
```