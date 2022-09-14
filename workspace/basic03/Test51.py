'''
데이터 저장
* 파이썬 - Oracle DB 연동 *
1. 라이브러리 설치
    - cx-Oracle (pycham)  cx_oracle (pip install cx_oracle)
    - oracle instant client 다운
'''
import datetime

import cx_Oracle

# 오라클 인스턴스 클라이언트 경로 지정
cx_Oracle.init_oracle_client(lib_dir=r'C:\oracle\instantclient_19_16')
'''
cx_Oracle.connect : 오라클 커넥션 접속 ('username','password','url:port/sid')
.cursor : 쿼리실행, 결과 데이터 담을 변수 선언
.execute : SQL 실행 , 결과가 cursor에 담김
.fetall : 쿼리실행 결과에서 데이터를 한 행씩 fetch 한다. 전부 all
.description : 데이터의 컬럼명 추출
'''
conn = cx_Oracle.connect('java04','java04','192.168.100.250:1521/orcl')
cursor = conn.cursor() # cursor 객체 얻어오기

# 데이터 조회
sql = 'select * from test'
cursor.execute(sql) # 쿼리문 실행
'''
for result in cursor:   # 커서에 담긴 결과를 하나씩 추출
    print(result)       # 튜플 형태
    print(result[0]) # ID
    print(result[1]) # PW
    print(result[2]) # Age 
    print(result[3]) # date
    print('='*50)

# 사용후 닫기
cursor.close()
conn.close()
'''
"""
# 데이터 저장
sql = 'insert into test values(:1, :2, :3, :4)'
data = ('py01','1234',20,datetime.datetime.now()) # 바인딩 시킬 데이터 튜플형태로 만들고
cursor.execute(sql, data)

# 커밋하고 닫기
cursor.close()
conn.commit()   # 커밋
conn.close()
"""
'''
# 데이터 여러개 추가
sql = 'insert into test values(:1, :2, :3, :4)'
data = [
    ('py02', '1234', 20+1, datetime.datetime.now()),
    ('py03', '1234', 20+2, datetime.datetime.now()),
    ('py04', '1234', 20+3, datetime.datetime.now()),
    ('py05', '1234', 20+4, datetime.datetime.now())
]
cursor.arraysize = len(data)
cursor.executemany(sql, data)       # 한번에 여러 레코드 insert

cursor.close()
conn.commit()
conn.close()
'''
'''
# 레코드 개수 조회
sql = 'select count(*) from test'
cursor.execute(sql)
count = cursor.fetchone() # 쿼리문 실행 결과에서 레코드 한개 추출
print(count)
print("회원수 :", count[0], "명")

cursor.close()
conn.close()
'''
"""
# 데이터 수정
sql = 'update test set pw=:1, age=:2 where id=:3'
data = ('9876', 98, 'py01')
cursor.execute(sql, data)

cursor.close()
conn.commit()
conn.close()
"""
"""
# 레코드 삭제
sql = "delete from test where id=:1"
data = ('py01',) # 튜플 형태로 데이터 생성
cursor.execute(sql, data)

cursor.close()
conn.commit()
conn.close()
"""









































