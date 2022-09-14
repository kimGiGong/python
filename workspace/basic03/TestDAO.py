import cx_Oracle
import datetime


class TestDAO:

    def __init__(self):
        cx_Oracle.init_oracle_client(lib_dir=r'C:\oracle\instantclient_19_16')


    def selectOne(self, id):
        conn = cx_Oracle.connect('java04', 'java04', '192.168.100.250:1521/orcl')
        cursor = conn.cursor()
        sql = 'select * from test where id=:1'
        cursor.execute(sql, id)
        print(cursor.fetchone())
        cursor.close()
        conn.close()

    def selectAll(self):
        conn = cx_Oracle.connect('java04', 'java04', '192.168.100.250:1521/orcl')
        cursor = conn.cursor()
        sql = 'select * from test'
        cursor.execute(sql)
        for row in cursor:
            print(row)
        cursor.close()
        conn.close()

    def insertUser(self, data):
        conn = cx_Oracle.connect('java04', 'java04', '192.168.100.250:1521/orcl')
        cursor = conn.cursor()
        sql = 'insert into test values(:1, :2, :3, :4)'
        # 바인딩 시킬 데이터 튜플형태로 만들고
        cursor.execute(sql, data)
        cursor.close()
        conn.commit()
        conn.close()

    def update(self, data):
        conn = cx_Oracle.connect('java04', 'java04', '192.168.100.250:1521/orcl')
        cursor = conn.cursor()
        sql = 'update test set pw=:1, age=:2 where id=:3'
        cursor.execute(sql, data)
        cursor.close()
        conn.commit()
        conn.close()

    def delete(self, data):
        conn = cx_Oracle.connect('java04', 'java04', '192.168.100.250:1521/orcl')
        cursor = conn.cursor()
        sql = "delete from test where id=:1"
        cursor.execute(sql, data)
        cursor.close()
        conn.commit()
        conn.close()


dao = TestDAO()
dao.selectAll()
print('ㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃ')
dao.selectOne(('py03',))  # tuple 형태로 인자 전달
# dao.insertUser(('python001','1234',1234,datetime.datetime.now()))
dao.selectAll()
dao.update(('1234', 4321, 'python001'))
dao.selectOne(('python001',))
print('ㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃ')
dao.delete(('python001',))