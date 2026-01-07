import pymysql
def CreateConn():
    return pymysql.connect(host = 'localhost', database = 'pramodwadekar', user = 'root',
    password='pramod123', port=3306 )

def deletedata(id):
    conn =  CreateConn()
    cursor = conn.cursor()
    args = (id)
    query = 'delete from student where id = %s'
    cursor.execute(query,args)
    conn.commit()
    print("Data Deleted")
    conn.close()
id = int(input('Enter Id Number = '))
deletedata(id)
