import pymysql

# 1. 직접 입력

# db 객체 생성
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='0000',
    database='solodb',
    charset='utf8'
)

# 커서 생성
cur = conn.cursor()

# table 초기화
cur.execute(
    'drop table userTable'
)

# table 생성
cur.execute(
    'create table userTable (id char(6), userName char(15), email char(20), birthYear int)'
)

# 데이터 주입
cur.execute(
    'insert into userTable values("hong1", "홍지윤1", "hong1@abc.com", 2001)'
)
cur.execute(
    'insert into userTable values("hong2", "홍지윤2", "hong2@abc.com", 2002)'
)
cur.execute(
    'insert into userTable values("hong3", "홍지윤3", "hong3@abc.com", 2003)'
)
cur.execute(
    'insert into userTable values("hong4", "홍지윤4", "hong4@abc.com", 2004)'
)

# transaction flush 및 resource 반환
conn.commit()
conn.close()



# 2. 콘솔 프로그램

# db 객체 생성
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='0000',
    database='solodb',
    charset='utf8'
)

cur = conn.cursor()

# 입력 로직
while True:
    data1 = input("ID: ")
    if data1 == "":
        break
    data2 = input("이름: ")
    data3 = input("이메일: ")
    data4 = input("출생년도: ")
    # sql 문 안에 data 를 주입해 sql 생성 ( 더 편한 방법이 분명 있을 것임 )
    sql = "insert into userTable values('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 +")"
    # sql 실행
    cur.execute(sql)

# flush 및 resource 반환
conn.commit()
conn.close()