import pymysql

# DB 객체 생성
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='0000',
    database='solodb',
    charset='utf8'
)

# db의 cursur 생성 ( sql 관련 작업들을 진행 )
cur = conn.cursor()

# db 객체에 sql 실행 
cur.execute("select * from userTable")

# 조회 로직
while True:
    # fetchone == record 를 하나씩 끌어올림 (fetchmany 도 있는 걸 보니 여러 개도 한 번에 가능한 듯)
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    # 출력
    print("%5s %15s % 20s %d" % (data1, data2, data3, data4))

# resource 반환
conn.close()