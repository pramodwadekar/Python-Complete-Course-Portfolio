import pymysql

def connection():
    return pymysql.connect(host= "localhost", port = 3306, user = "root", database = "pramodwadekar", password = "Pramod@123")

def droptable():
    conn = connection()
    cursor =conn.cursor()
    query = "drop table user"
    cursor.execute(query)
    conn.commit()
    print("table drop successfull")
    conn.close()

droptable()