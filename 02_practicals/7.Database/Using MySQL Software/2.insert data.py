import pymysql
def CreateConn():
    return pymysql.connect(host="localhost", database='pramodwadekar', user='root', password ='Pramod@123', port=3306 )

def insertdata(Name,Email,City):
    conn = CreateConn()
    cursor = conn.cursor()
    args = (Name,Email,City)
    query = 'insert into user (Name,Email,City)value (%s,%s,%s)'
    cursor.execute(query,args)
    conn.commit()
    print("data inserted")
    conn.close()
n = input('enter your name :-')
e = input('enter your email :-')
c = input('enter your city name :-')
insertdata(n,e,c)