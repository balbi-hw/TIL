"""
링크드 리스트는 딱히 아닌듯?

메모리 풀
id 번호를 인덱스 값으로 쓰는 리스트를 만들고 그 리스트 안에
팀, 개인 평판 을 담고 ( 1 <= mID <= 100,000 )
팀 번호를 인덱스 값으로 쓰는 리스트 추가, 팀 평판 저장 ( 1 <= mTeam <= 5)
"""

def init():
    global id_list, team_list, team_member

    id_list = [[] for _ in range(100001)]
    team_list = [0] * 6
    team_member = [[] for _ in range(6)]


def hire(mID, mTeam, mScore):
    id_list[mID] = [mTeam, mScore]
    team_member[mTeam].append(mID)
    pass

def fire(mID):
    team = id_list[mID][0]
    team_member[team].remove(mID)
    id_list[mID] = []
    pass

def updateSoldier(mID, mScore):
    id_list[mID][1] = mScore
    pass


"""
핵심 병목 // 단순 for 문으로 처리해서 병목이 생겼다. 비트마스킹?
"""
def updateTeam(mTeam, mChangeScore):

    for i in team_member[mTeam]:
        id_list[i][1] += mChangeScore

        if id_list[i][1] > 5:
            id_list[i][1] = 5
        elif id_list[i][1] < 1:
            id_list[i][1] = 1
    pass

def bestSoldier(mTeam):

    """
    이 sort 도 너무 비효율적인 것 같은데 어떻게 해결해야하지?
    """
    try:
        team_member[mTeam].sort(key=lambda x: (-id_list[x][1], -x))
    except IndexError:
        pass
    
    # print(id_list[team_member[mTeam][0]])
    # print(team_member[mTeam][0])
    return team_member[mTeam][0]

    pass

# 소스코드와 같은 디렉토리에 input.txt 파일을 생성해서 거기에 입력을 넣은 뒤 아래 주석을 지우면 편하게 실행 가능합니다 :)
fs = open("input.txt", "r")
input = fs.readline

CMD_INIT = 1
CMD_HIRE = 2
CMD_FIRE = 3
CMD_UPDATE_SOLDIER = 4
CMD_UPDATE_TEAM = 5
CMD_BEST_SOLDIER = 6

def run():
    isCorrect = False
    numQuery = int(input())

    for i in range(numQuery):
        line = list(map(int, input().split()))
        cmd = line[0]

        if cmd == CMD_INIT:
            init()
            isCorrect = True
        elif cmd == CMD_HIRE:
            mID, mTeam, mScore = line[1], line[2], line[3]
            hire(mID, mTeam, mScore)
        elif cmd == CMD_FIRE:
            mID = line[1]
            fire(mID)
        elif cmd == CMD_UPDATE_SOLDIER:
            mID, mScore = line[1], line[2]
            updateSoldier(mID, mScore)
        elif cmd == CMD_UPDATE_TEAM:
            mTeam, mChangeScore = line[1], line[2]
            updateTeam(mTeam, mChangeScore)
        elif cmd == CMD_BEST_SOLDIER:
            mTeam = line[1]
            userAns = bestSoldier(mTeam)
            ans = line[2]
            if userAns != ans:
                isCorrect = False
        else:
            isCorrect = False

    return isCorrect

T, MARK = map(int, input().split())

id_list = None
team_list = None
team_member = None

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print(f'#{tc} {score}')
