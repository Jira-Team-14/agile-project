from getpass import getpass
from mysql.connector import connect, Error


# This is a class for editing employees and buildings into the db
class modifyTable:
    def __init__(self,connection):
        self.connection=connection

    def showEmployee(self,id):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT * 
            FROM agile_project.employee
            WHERE employee_id = {} ;""".format(id)
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(e)
            return e

    def editEmployee(self,infoTuple):
        try:
            n = 'none'
            cursor = self.connection.cursor()
            query = """
        UPDATE agile_project.employee SET  name=%s, address=%s, date_of_birth=%s, salary=%s, contact_info=%s, date_of_employement=%s, supervisor_id=%s WHERE employee_id = %s;"""
            with self.connection.cursor() as cursor:
                isDone = cursor.execute(query, infoTuple)
                self.connection.commit()        #if you do not commit the change  is automatically rolledback
                if (str(isDone).lower() == n):      #the cursor returns the errors found during execution, reterning none if it executed successfuly
                    return isDone
                else:
                    return "false"
        except Error as e:
            return e

    def deleteEmployee(self,id):
        try:
            n = 'none'
            cursor = self.connection.cursor()
            query = """
        DELETE FROM agile_project.employee 
        WHERE
            employee_id = {};""".format(id)
            with self.connection.cursor() as cursor:
                isDone = cursor.execute(query)
                self.connection.commit()        #if you do not commit the change  is automatically rolledback
                if (str(isDone).lower() == n):      #the cursor returns the errors found during execution, reterning none if it executed successfuly
                    return isDone
                else:
                    return "false"
        except Error as e:
            return e


    def deletebuilding(self,id):
        try:
            n = 'none'
            cursor = self.connection.cursor()
            query = """
        DELETE FROM agile_project.building 
        WHERE
            employee_id = {};""".format(id)
            with self.connection.cursor() as cursor:
                isDone = cursor.execute(query)
                self.connection.commit()        #if you do not commit the change  is automatically rolledback
                if (str(isDone).lower() == n):      #the cursor returns the errors found during execution, reterning none if it executed successfuly
                    return isDone
                else:
                    return "false"
        except Error as e:
            return e

    def showBuilding(self,id):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT * 
            FROM agile_project.building
            WHERE building_id = {} ;""".format(id)
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(e)
            return e

    def editBuilding(self, infoTuple):
        try:
            n = 'none'
            cursor = self.connection.cursor()
            query = """
        UPDATE agile_project.building SET  location=%s, total_floor=%s WHERE building_id = %s;"""
            with self.connection.cursor() as cursor:
                isDone = cursor.execute(query, infoTuple)
                self.connection.commit()  # if you do not commit the change  is automatically rolledback
                if (
                        str(isDone).lower() == n):  # the cursor returns the errors found during execution, reterning none if it executed successfuly
                    return isDone
                else:
                    return "false"
        except Error as e:
            return e
