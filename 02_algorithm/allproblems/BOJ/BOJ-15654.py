# BOJ - 15654  N과 M
# 실패

import sys
sys.setrecursionlimit(10**7)

class Integer:
    def __init__(self, word):
        self.word = word
        pass

    def add_char(self, char):
        self.word += char
        pass

    def remove_char(self, char):
        self.chars = list(self.word)
        for i in range(len(self.chars)-1, -1, -1):
            if self.chars[i] == char:
                self.chars.remove(char)
                break
        self.word = "".join(self.chars)

    def get_word(self):
        return self.word

    def length(self):
        return len(self)


def dfs(N: int, M: int, nums: list, visited: list, result: list, string: Integer) -> None:
    global lst

    for idx in range(N):
        if not visited[idx]:
            visited[idx] = True
            string.add_char(nums[idx])

            if len(string.get_word()) == M:
                result.append(string.get_word())
            
            if len(result) == M:
                lst.append(*result)
                result.pop()

            dfs(N, M, nums, visited, result, string)
            
            visited[idx] = False
            string.remove_char(nums[idx])
            # if result:
            #     result.pop()
    
    return

N, M = map(int, input().split())
nums = input().split()
visited = [False] * N

result = []
string = Integer("")
lst = []
dfs(N, M, nums, visited, result, string)

print(lst)
lst.sort()
print(*lst)