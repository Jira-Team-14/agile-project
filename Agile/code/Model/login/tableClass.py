from getpass import getpass
from mysql.connector import connect, Error


class logintable:
    def __init__(self,type):
        self.type = type

    def getloginquery(self):
        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="agile_project",
            ) as connection:
                print(connection)
                cursor = connection.cursor()
                print("OKE")
                get_login_query = """
                SELECT id,password 
                FROM agile_project.login
                WHERE type = {} ;""".format(self.type)
                with connection.cursor() as cursor:
                    cursor.execute(get_login_query)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
        except Error as e:
            print(e)

