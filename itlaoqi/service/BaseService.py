import pymysql.cursors


class BaseService:
    def get_connection(self):
        # Connect to the database
        connection = pymysql.connect(host='himcs.io',
                                     user='root',
                                     password='root',
                                     database='itlaoqi',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection

    def fetchall(self, query, args=None):
        connection = self.get_connection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query, args)
                result = cursor.fetchall()
                return result
