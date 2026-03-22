# Disjoint Set - 서로소 집합

[연습문제](#연습문제)

- 서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들이다. ( 교집합이 없다. )
- 두 집합 간에 공통 원소가 하나도 없을 때 두 집합을 서로소 집합이라고 한다.
- 집합에 속한 하나의 특정 멤버를 통해 각 집합을 구분한다. ( 대표자 )

---

## 상호배타 집합 연산

1. Make-set
    - 집합을 생성하기

2. Find-set
    - 집합의 대표자 찾기

3. Union
    - 두 집합을 합치기

---

## 서로소 집합 표현

1. 연결 리스트
    - 직관적이지만 시간복잡도가 트리 표현에 비해 높다
2. 트리
    - 시간복잡도가 연결 리스트에 비해 낮다.

---

## 코드 구현

1. Make-set
```python
p = [0] * (N+1)

def make_set(x):
    p[x] = x
```
  
2. Find-set
```python
def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])
```
  
3. Union
```python
def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px < py:
        p[py] = px
    else:
        p[px] = py
```
  
4. Overall
```python
p = [0] * (N+1)

def make_set(x):
    p[x] = x

def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px < py:
        p[py] = px
    else:
        p[px] = py
```

## 조금의 최적화

1. 
```python
def make_set(n):
    return [i for i in range(n + 1)]
'''
초기 트리 구현 없이 함수만으로 구현 가능
'''
```

2. Path Compression, 경로 압축
- 특정 노드에서 루트까지의 경로를 찾아 가면서 부모 노드를 갱신.
```python
# 전
def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])

# 최적화 후
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]
```
  
3. Rank를 이용한 Union
- 결합을 할 때 랭크가 낮은 트리를 더 높은 트리에 붙인다.
    - 랭크가 서로 다르면 결합 후 트리의 랭크는 둘 중 더 큰 트리의 랭크 ( 변화 없음 )
    - 둘이 같다면 결합후 랭크는 ( 결합 전 랭크 + 1 )
- 랭크 기록 리스트가 하나 더 필요하다.
```python
p = [0] * (N + 1)
rank = [0] * (N + 1)

def make_set(x):
    p[x] = x

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[py] < rank[py]:
            p[px] = py
        else:
            p[py] = px
            rank[px] += 1
```

### 연습문제

```python
# SWEA - 14163  그룹 나누기

def make_set(n):
    return [i for i in range(n+1)]

def find_set(x):
    if x != tree[x]:
        tree[x] = find_set(tree[x])
    return tree[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px < py:
        tree[py] = px
    else:
        tree[px] = py

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))

    tree = make_set(N)
    for i in range(M):
        p, c = info[i*2], info[i*2+1]
        union(p, c)

    #####
    for i in range(1, N+1):
       tree[i] = find_set(i)
    #####

    result = set(tree[1:])
    print(f"#{test_case} {len(result)}")
```
어느 정도 구현은 헀었는데 해결은 실패한 문제.
- Record
1. 인접리스트로 풀면 되는거 아닌가? 싶어서 시도했는데 인접리스트는 대표자를 찾지 못함. 해당 노드의 부모만 찾을 수 있다.
```python
for i in range(M):
    p, c = info[i*2], info[i*2+1]
    tree[c] = tree[p]  # 이 위로 올라가는게 불가능
```
2. tree[i]와 find_set[i] 는 다를 수 있다.  
코드에 주석으로 감싸둔 부분이 필수적이다.  
처음엔 그냥 union 함수를 통해 트리 병합만 하면 끝날 줄 알았는데, 병합의 순서에 따라 그렇지 않을 수 있다는 걸 간과했다.  
예를 들어 `union(4, 5) > union(3, 4) > union(2, 3) > union(1, 2)` 순서로 진행되면 최종 트리는 `tree = [0, 1, 1, 2, 3, 4]` 형태가 된다.  
이 트리는 분명 하나의 트리이지만 각 인덱스의 값이 대표자를 가리키지 않기 때문에 문제가 생긴다.