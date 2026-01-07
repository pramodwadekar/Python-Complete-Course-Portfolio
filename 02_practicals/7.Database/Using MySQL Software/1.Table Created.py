import pymysql
def CreateConn():
    return pymysql.connect(host="localhost", database='pramodwadekar', user='root', password ='Pramod@123', port=3306 )

def CreateTable():
    conn = CreateConn()
    cursor = conn.cursor()
    query = 'create table user(id int primary key auto_increment, name VARCHAR(50), email VARCHAR(50),city VARCHAR(50))'  
    cursor.execute(query)
    conn.commit()
    print('Table is created')
    conn.close()
CreateTable()