import sys
sys.stdin = open('input.txt')

# 총 8개 숫자
# 앞 7자리는 상품 고유번호, 마지막 검증코드
# 홀수 * 3 + 짝수 + 검증 = 10의 배수

# 16진수로 주어지며 2진수 변환 후 코드 확인
# 비정상 코드 포함


# 역순으로 돌면서 처음 만나는 1부터 카운팅 시작
# 0 만나면 그때까지 카운팅 기록 후 다시 카운팅
# a, b, c, d 다 찰때까지 반복. d부터 채우면 직관적일듯
# a : b : c : d 비율로 배율 구하고 ( 제일 작은 걸로 나누면 되겠다. // 그냥 제일 작은 수가 배율이네 )
# 처음 1 만난 인덱스도 기록해뒀다가 idx -= (56*배수)
# 하면 시작점이 나온다.
# 맵핑을 abcd : num 으로 해야겠는데
# 그럼 배율 구할 필요도 딱히 없나?

# 암호가 여러개 있는 배열도 있으니까 여러번 해야하는데
# 좌표를 저장해야겠다
# 덩어리를 나누고 싶은데 BFS를 넣으면 좀 무거워질 것 같다. 그래도 넣어볼까
# 아니면 그냥 순회?
# 근데 이러면 처음부터 끝까지 다 봐야한다는게 좀 에바네 ( 시간 제한 30초 // 그냥 하라고 만든 듯? )
# 적어도 열은 56까지만 보면 되는데 행은 다봐야함


from collections import deque

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs(r, c):
    global visited

    q = deque([(r, c)])
    visited[r][c] = True

    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if not (0 <= nr < N and 0 <= nc < M):
                continue

            if visited[nr][nc]:
                continue

            if code[nr][nc] == "0":
                if code[nr+dr][nc+dc] == '0':
                    continue

            visited[nr][nc] = True
            q.append((nr, nc))


TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())

    # 8개의 숫자
    # 7개의 비트로 암호화
    mapping = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9',
        '3 2 1 1': '0',
        '2 2 2 1': '1',
        '2 1 2 2': '2',
        '1 4 1 1': '3',
        '1 1 3 2': '4',
        '1 2 3 1': '5',
        '1 1 1 4': '6',
        '1 3 1 2': '7',
        '1 2 1 3': '8',
        '3 1 1 2': '9'
    }

    code = [input().strip() for r in range(N)]
    visited = [[False] * M for _ in range(N)]

    start_spots = []
    pwd_lst = set()

    # 행 두께가 정해져있긴 한데 값이 작아서 하나마나일듯
    # 진법 변환부터 해야겠다.
    # 다 할 수는 없으니까 암호 있는 행을 만나면
    # 문자열 초기화하고 bfs 돌리고 다시 돌다가 visited 안된 자리 만나면 문자열 끝 
    for r in range(N-1, -1, -1):
        enigma = ""
        for c in range(M-1, -1, -1):  # 그냥 다 돌자 복잡하다.
            if code[r][c] != '0':
                bfs(r, c)  # 여기서 한 덩어리 전부 방문처리 됨

            if visited[r][c]:  # 방문처리가 된 곳이면
                enigma += code[r][c]  # 암호에 추가
            # 이 청크로 인해 집합에 공백이 하나 추가되는데 큰 결점은 아닌듯해서 다 하고 remove로 제거
            else:
                if enigma not in pwd_lst:  
                    pwd_lst.add(enigma[::-1])  # 역순으로 돌았으니 뒤집어서
                    enigma = ""
    # 공백 제거
    pwd_lst.remove('')
    pwd_lst = list(pwd_lst)

    # 진법 변환
    mapping2 = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    binary_lst = []
    # nbinary = ""
    for hexa in pwd_lst:
        nbinary = ""

        if len(hexa) < 16:
            hexa = '0' + hexa

        for char in hexa:
            nbinary += mapping2[char]
        

        idx = 0
        for i in range(len(nbinary)-1, -1, -1):
            if nbinary[i] != "0":
                idx = int(i)
                break

        binary_lst.append(nbinary[idx-55:idx+1])

    # print(binary_lst)

    point = 1
    final_binary_lst = []     

    for binary in binary_lst:
        print(len(binary))
        final_lst = []

        while point < 55:

            # 그럼 이제 앞에서부터 보면서 비율 계산
            num_lst = [0, 0, 0, 0]
            # for binary in binary_lst:
                # 모든 숫자의 시작은 0, 끝은 1
            run = 1
            for i in range(4):
                for j in range(point, len(binary)):
                    if j == len(binary):
                        if binary[j] == binary[j-1]:
                            run += 1
                            num_lst[i] = run
                            point += 1
                            break
                        else:
                            num_lst[i] = run
                    else:
                        if binary[j] != binary[j-1]:
                            num_lst[i] = run
                            run = 1
                            point = j + 1
                            break
                        else:
                            run += 1
                    # run += 1
            if len(final_lst) < 8:
                if num_lst[3] == 0:
                    num_lst[3] = run
                final_lst.append([i // min(num_lst) for i in num_lst])

        final_binary_lst.append(final_lst)

    # print(*final_lst)
    # print(num_lst)

    result_lst = [0]
    total_lst = []

    while final_binary_lst:

        pwd = ""

        final_lst = final_binary_lst.pop()
        
        for lst in final_lst:
            temp = " ".join(map(str, lst))
            pwd += mapping[temp]
        
        # print(pwd)

        odd = 0
        even = 0

        for idx in range(len(pwd)):
            if (idx + 1) % 2 == 1:
                odd += int(pwd[idx])
            else:
                even += int(pwd[idx])
        
        total = odd * 3 + even

        if total % 10 == 0:
            total_lst.append(odd + even)

    print(f"#{test_case} {sum(total_lst)}")
    #     print(total)

    # if total % 10 == 0:
    #     result_lst.append(odd + even)
    
    # print(f'#{test_case} {sum(result_lst)}')