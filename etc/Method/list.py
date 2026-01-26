################ 리스트 값 추가 및 삭제 ################

# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
# append는 None을 반환합니다.
print(my_list.append(4))  # None

# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]

# extend와 append의 비교
my_list.append([5, 6, 7])
print(my_list)  # [1, 2, 3, 4, 5, 6, [5, 6, 7]]

# my_list.extend(100)  # TypeError: 'int' object is not iterable

# insert
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  # [1, 5, 2, 3]

# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]

# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4]

# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []


################ 리스트 정렬 및 순서 변경 ################

# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
# reverse는 None을 반환합니다.
# print(my_list.reverse())  # None
# reverse는 원본 리스트를 변경합니다.
print(my_list)  # [9, 1, 8, 2, 3, 1]

# sort
my_list = [3, 2, 100, 1]
my_list.sort()
# sort는 None을 반환합니다.
# print(my_list.sort())  # None
# sort는 원본 리스트를 변경합니다.
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]
