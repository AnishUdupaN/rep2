import pymysql
import sys
def connect_db():
    try:
        connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='abcd_db',charset='utf8')
        print('DB connected. ')
        return connection
    except:
        print('DB connection failed. ')
        sys.exit(0)
def disconnect_db(connection):
    try:
        connection.close()
        print('DB disconnected. ')
    except:
        print("DB disconnection failed. ")
#connection=connect_db()
#disconnect_db(connection)

def create_db():
    connection=connect_db()
    query='create database if not exists abcd_db1;'
    cursor=connection.cursor()
    cursor.execute(query)
    cursor.close()
    disconnect_db(connection)



def create_table():
    connection=connect_db()
    query="create table if not exists people(id int primary key,name varchar(30) not null,gender char check(gender in('m','M','f','F')),location varchar(50),dob datetime);"
    cursor=connection.cursor()
    cursor.execute(query)
    cursor.close()
    disconnect_db(connection)

create_table()