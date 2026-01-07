import pymysql 

def connection():
    return pymysql.connect(host="localhost", port = 3306, user ="root" , database = "pramodwadekar", password = "Pramod@123")

def dropdatabase():
    conn = connection()
    cursor = conn.cursor()
    query = "drop database pramodwadekar"
    cursor.execute(query)
    conn.commit()
    print("database drop successfull")
    conn.close()
dropdatabase()