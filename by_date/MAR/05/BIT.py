# 수업 내용

# 아 비트연산은 진리표로 연산하는거야?




'''
비트연산
- 자리수가 1인지 0인지 비교하기 위해 사용
  - True False 배열 만들때 좋네

'''

arr = [7, 1, 3, 5]
print(1 << len(arr))

for i in range(1<<len(arr)):
    print(f"{i} 번 째 부분집합: ", end=' ')
    for idx in range(len(arr)):
        if i & (1 << idx):
            print(arr[idx], end=' ')
    print()
    pass