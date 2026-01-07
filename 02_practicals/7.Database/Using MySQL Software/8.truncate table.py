import pymysql
def CreateConn():
    return pymysql.connect(host="localhost", database='pramodwadekar', user='root', password ='Pramod@123', port=3306 )

def showalldata():
    conn = CreateConn()
    cursor = conn.cursor()
    query = "truncate table user"
    cursor.execute(query)
    conn.commit()
    print("table Truncate")
    conn.close()
showalldata()