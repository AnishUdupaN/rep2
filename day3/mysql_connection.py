import pymysql

def connect_db(user,password):
    try:
        connection = pymysql.Connect(host='localhost', port=3306, user=user, password=password, database='AnishUdupaN', charset='utf8')
        print('DB connected')
        return connection
    except:
        print('DB connection failed')

def disconnect_db(connection):
    try:
        connection.close()
        print('DB disconnected')
    except:
        print('Error while disconnecting DB')

connection = connect_db('root','root')
if connection:
    disconnect_db(connection)