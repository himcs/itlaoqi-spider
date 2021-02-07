import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='himcs.io',
                             user='root',
                             password='root',
                             database='itlaoqi',
                             cursorclass=pymysql.cursors.DictCursor)
with connection:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * from catalogue"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
