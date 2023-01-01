from getpass import getpass
from mysql.connector import connect, Error


# This is a class for DATABASE TABLE "LOGIN" query methods
class logintable:
    def __init__(self,type,connection):
        self.type = type
        self.connection=connection
    def getloginquery(self):
        try:
            print(self.connection)
            cursor = self.connection.cursor()
            get_login_query = """
            SELECT id,password 
            FROM agile_project.login
            WHERE type = {} ;""".format(self.type)
            with self.connection.cursor() as cursor:
                cursor.execute(get_login_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)
                return result
        except Error as e:
            print(e)
            return e

    def gui_msgs(self):
        try:
            cursor = self.connection.cursor()
            get_query = """
            SELECT msg FROM agile_project.gui_msgs;"""
            with self.connection.cursor() as cursor:
                cursor.execute(get_query)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(e)
            return e