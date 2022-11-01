from getpass import getpass
from mysql.connector import connect, Error

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
        insert_login_query = """
        SELECT * FROM agile_project.login;"""
        with connection.cursor() as cursor:
            cursor.execute(insert_login_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)



