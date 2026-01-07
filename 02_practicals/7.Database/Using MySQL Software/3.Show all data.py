import pymysql

def CreateConn():
    return pymysql.connect(host="localhost", database='pramodwadekar', user='root', password ='Pramod@123', port=3306 )

def showalldata():
    conn = CreateConn()
    cursor = conn.cursor()
    query = "select *from user"
    cursor.execute(query)
    result =cursor.fetchall()
    for i in result:
        print(i)
showalldata()