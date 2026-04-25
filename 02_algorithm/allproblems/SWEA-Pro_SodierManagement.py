"""
링크드 리스트는 딱히 아닌듯?

메모리 풀
id 번호를 인덱스 값으로 쓰는 리스트를 만들고 그 리스트 안에
팀, 개인 평판 을 담고 ( 1 <= mID <= 100,000 )
팀 번호를 인덱스 값으로 쓰는 리스트 추가, 팀 평판 저장 ( 1 <= mTeam <= 5)

객체로 관리하자.
1. 전체 리스트 // 인덱스로 개체
2. 팀별 리스트 // 여기도 인덱스로 객체?

100_000 리스트 6개 ?


"""
from collections import deque


# MAP = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five',
# }


# class LinkedList():
#     def __init__(self):
        
#         pass

#     def extend(self):
#         pass



"""

개선할 사항

1. 현재 member.score 와 team.member.score 가 안맞고 있음
   인스턴스 score 변동을 team 점수 리스트에 반영해야한다. 아님 반대라도 해야한다.

2. Team 의 update 메서드도 로직 개선 필

둘 다 해결한 것 같은데

1번 테케 15 ~ 17 번 쿼리 사이에 문제가 있음

"""


"""
또 다시 시간 최적화.. 우선 update 가 병목이 심함 얘만 해결하면 될 것 같은데

팀 스코어와 멤버 스코어를 연결할 수 없을까?

팀스코어?

팀 스코어 업데이트를 기록해뒀다가 나중에 계산? 
"""


class Member():
    def __init__(self, mID, mTeam, mScore):
        self.mID = mID
        self.mTeam = mTeam
        self.mScore = mScore
        self.next = None

    def get_id(self):
        return self.mID

    def get_team(self):
        return self.mTeam

    def get_score(self):
        return self.mScore
    
    def set_score(self, mScore):
        self.mScore = mScore


class Team():
    def __init__(self):
        self.members = [[] for _ in range(6)]


    def get_members(self, mScore):
        return self.members[mScore]
    
    def update(self, mChangeScore):
        if mChangeScore < 0:
            for i in range(1, 6):
                val = i + mChangeScore
                if val > 5:
                    val = 5
                elif val < 1:
                    val = 1
                
                if i == val:
                    continue

                self.members[val].extend(self.members[i])
                for member in self.members[i]:
                    member.set_score(val)
                self.members[i].clear()

        if mChangeScore > 0:
            for i in range(5, 0, -1):
                val = i + mChangeScore
                if val > 5:
                    val = 5
                elif val < 1:
                    val = 1
                
                if i == val:
                    continue

                self.members[val].extend(self.members[i])
                for member in self.members[i]:
                    member.set_score(val)
                self.members[i].clear()
            
        
        pass

    def get_best(self, mTeam):

        """오프셋 다 적용하고 계산해야한다."""
        for i in range(1, 6):
            idx = i + TeamOffset[mTeam][i]
            self.members[idx].extend(self.members[i])

        for i in range(5, 0, -1):
            self.members[i].sort(key=lambda x: -x.mID)
            for member in self.members[i]:
                if not member:
                    continue
                elif FiredMemberList[member.mID]:
                    continue
                else:
                    return member.mID
            
        return 1
        pass


"""
헤드, 트레일, 최고id, 메서드, 병합,
"""

class LinkedList():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    
    """인덱스 유지할 필요 있나?"""
    def add(self, member):
        if self.first == None:
            self.first = member
        else:
            self.first.next = member
        self.last = member            
        self.size += 1

    def extend(self, linkedList):
        if linkedList.first == None:
            return
        self.last.next = linkedList.first
        self.size += linkedList.size
        self.last = linkedList.last
    


    pass


MemberList = [None for _ in range(100_001)]
FiredMemberList = [False] * 100_001
TeamList = [Team() for _ in range(6)]
TeamOffset = [[0] * 6 for _ in range(6)]


def init():
    global MemberList, TeamList, FiredMemberList, TeamOffset
    MemberList = [None for _ in range(100_001)]
    FiredMemberList = [False] * 100_001
    TeamList = [Team() for _ in range(6)]
    TeamOffset = [[0] * 6 for _ in range(6)]

def hire(mID, mTeam, mScore):
    member = Member(mID, mTeam, mScore + TeamOffset[mTeam][0])
    MemberList[mID] = member
    TeamList[mTeam].get_members(mScore).append(member)
    pass

def fire(mID):
    FiredMemberList[mID] = True
    pass

def updateSoldier(mID, mScore):
    member = MemberList[mID]
    member.set_score(mScore + TeamOffset[member.mTeam])

    pass

def updateTeam(mTeam, mChangeScore):
    # TeamList[mTeam].update(mChangeScore)
    # TeamOffset[mTeam] += mChangeScore
    for i in range(1, 6):
        TeamOffset[mTeam][i] += mChangeScore
        if i + TeamOffset[mTeam][i] > 5:
            TeamOffset[mTeam][i] = 5 - i
        elif i + TeamOffset[mTeam][i] < 1:
            TeamOffset[mTeam][i] = 1 - i
    pass

def bestSoldier(mTeam):
    return TeamList[mTeam].get_best(mTeam)
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

            # print(userAns, ans)

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
