# 얕은 복사와 깊은 복사의 개념
# 복사 대상이 다차원으로 넘어가면 얕은 복사는 내부의 내부까지는 복사하지 못한다.
# data structure 이미지 추가 예정

# 대상이 복잡해질수록 깊은 복사는 필수적이고 깊은 복사를 하기 위해서는 copy 모듈을 import 해야한다. 깊은 복사를 하면 메모리는 두 배가 된다.
# import copy / copy.deepcopy


# 얕은 복사
print('\n얕은 복사 예시')

# 1차원 리스트에서의 얕은 복사 (리스트 슬라이싱)
a = [1, 2, 3]
b = a[:]

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]

# 1차원 리스트에서의 얕은 복사 (copy 메서드)
a = [1, 2, 3]
b = a.copy()

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]


# 1차원 리스트에서의 얕은 복사 (list() 함수)
a = [1, 2, 3]
d = list(a)
a[0] = 100
print(a)  # [100, 2, 3]
print(d)  # [1, 2, 3]


# 얕은 복사의 한계
print('\n다차원 리스트 얕은 복사의 한계')
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [999, 2, [3, 4, 5]]

b[2][1] = 100
print(a)  # [1, 2, [3, 100, 5]]
print(b)  # [999, 2, [3, 100, 5]]

print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # True


# 깊은 복사
import copy

print('깊은 복사 예시')
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100

print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [1, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # False

# 복잡한 중첩 객체 예시
print('복잡한 중첩 객체 깊은 복사')
original = {
    'a': [1, 2, 3],
    'b': {'c': 4, 'd': [5, 6]},
}
copied = copy.deepcopy(original)

copied['a'][1] = 100
copied['b']['d'][0] = 500

print(f'원본: {original}')  # {'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}
print(f'복사본: {copied}')  # {'a': [1, 100, 3], 'b': {'c': 4, 'd': [500, 6]}}
print(
    f"original['b']와 copied['b']가 같은 객체인가? {original['b'] is copied['b']}"
)  # False
