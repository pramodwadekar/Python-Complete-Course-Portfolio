import pymysql
def Createconn():
    return pymysql.connect(host = "localhost", database = "lernvern", user = "root",
    password = "pramod123", port = 3306)
    def CreateTable():
        conn = CReateConn()
        cursor = conn.cursor()
        query = "Create table student(sid int primary key auto_increament,name VARCHAR(50),email VARCHAR(50),City VARCHAR(50))"
        cursor.execute(query)
        connection.commit()
        print("Table Created")
        conn.close
        CreateTable()