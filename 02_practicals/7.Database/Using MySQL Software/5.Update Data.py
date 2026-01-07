import pymysql

def CreateConn():
    return pymysql.connect(host="localhost", database='pramodwadekar', user='root',
     password ='Pramod@123', port=3306 )

def updatedata(Name,Email,City,id):
    conn = CreateConn()
    cursor = conn.cursor()
    args = (Name,Email,City,id)
    query = "update user set Name = %s, Email = %s, City = %s where id = %s"
    cursor.execute(query,args)
    conn.commit()
    print ('data updated')
    conn.close()
id = int(input('Enter Id Number = '))
n = input('enter your name :-')
e = input('enter your email :-')
c = input('enter your city name :-')
updatedata(n,e,c,id)

