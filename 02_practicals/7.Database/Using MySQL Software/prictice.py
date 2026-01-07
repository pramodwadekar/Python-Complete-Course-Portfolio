#insert table 

# import pymysql
# def connection():
#     return pymysql.connect(host = "localhost", port = 3306, database = "company", user = "root", password = "Pramod@123")


# def create_table():
#     conn = connection()
#     cursor =conn.cursor()
#     query = "create table employee1 (id int auto_increment primary key, name varchar(50), email varchar(50), city varchar(50))"
#     cursor.execute(query)
#     conn.commit()
#     print ("Table is Created")
#     conn.close()
# create_table()

# import pymysql
# def connection():
#     return pymysql.connect(host = "localhost", database = "company", user = "root", port =3306, password = "Pramod@123")
# def create_table(name, email, city):
#     conn = connection()
#     cursor = conn.cursor()
#     args = (name,email,city)
#     query = "insert into employee (name,email,city)value(%s,%s,%s)"
#     cursor.execute(query, args)
#     conn.commit()
#     print("table is created")
#     conn.close()
# n = input("name :")
# e = input("email :")
# c = input("city :")
# create_table(n,e,c)

import pymysql
def connection():
    return pymysql.connect(host = "localhost", port = 3306, user = "root", database = "company", password ="Pramod@123")

def updatedata():
    conn = connection()
    cursor = conn.cursor()
    args = (id)
    query = "delete from employee where id = %s"
    cursor.execute(query,args)
    result =cursor.fetchall()
    for i in result:
        print(i)
    conn.commit()
    print("data Deleted")
    conn.close()
id = int(input("id :"))
updatedata()