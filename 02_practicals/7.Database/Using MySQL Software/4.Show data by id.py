import pymysql

def CreateConn():
    return pymysql.connect(host="localhost", database='pramodwadekar', user='root', password ='Pramod@123', port=3306 )

def showdatabyid():
    conn = CreateConn()
    cursor = conn.cursor()
    args = (id)
    query = "select *from user where id = %s"
    cursor.execute(query,args)
    result =cursor.fetchall()
    for i in result:
        print(i)
id = int(input('Enter Id Number :-'))
showdatabyid()