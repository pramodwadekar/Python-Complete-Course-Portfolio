import pymysql
def CreateConn():
    return pymysql.connect(host = 'localhost', database = 'mayur', user = 'root',
    password='', port=3306 )

def CreateTable():
    conn = CreateConn()
    cursor = conn.cursor()
    query = 'create table student(id int primary key auto_increment, Name VARCHAR(50), Email VARCHAR(50), City VARCHAR(50))' 
    cursor.execute(query)
    conn.commit()
    print('Table is created')
    conn.close()
CreateTable()

def insertdata(Name,Email,City):
    conn = CreateConn()
    cursor = conn.cursor()
    args = (Name,Email,City)
    query = 'insert into student (Name,Email,City)value (%s,%s,%s)'
    cursor.execute(query,args)
    conn.commit()
    print("data inserted")
    conn.close()
n = input('enter your name :-')
e = input('enter your email :-')
c = input('enter your city name :-')
insertdata(n,e,c)

def showalldata():
    conn = CreateConn()
    cursor = conn.cursor()
    query = "select *from student"
    cursor.execute(query)
    result =cursor.fetchall()
    for i in result:
        print(i)
showalldata()

def showdatabyid():
    conn = CreateConn()
    cursor = conn.cursor()
    args = (id)
    query = "select *from student where id = %s"
    cursor.execute(query,args)
    result =cursor.fetchall()
    for i in result:
        print(i)
showalldata()
id = int(input('Enter Id Number :-'))
showdatabyid()

def updatedata(Name,Email,City,id):
    conn = CreateConn()
    cursor = conn.cursor()
    args = (Name,Email,City,id)
    query = "update student set Name = %s, Email = %s, City = %s where id = %s"
    cursor.execute(query,args)
    conn.commit()
    print ('data updated')
    conn.close()
showalldata()
id = int(input('Enter Id Number = '))
n = input('enter your name :-')
e = input('enter your email :-')
c = input('enter your city name :-')
updatedata(n,e,c,id)
showalldata()


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
showalldata()