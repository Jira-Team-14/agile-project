from getpass import getpass
from mysql.connector import connect, Error


# This is a class for adding employees and buildings into the db
class addStakeholder:
    def __init__(self,connection):

        self.connection=connection

    def addEmployee(self,infoTuple):
        try:
            n = 'none'
            cursor = self.connection.cursor()
            addBAquery = """
        INSERT INTO agile_project.employee VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            with self.connection.cursor() as cursor:
                isDone = cursor.execute(addBAquery, infoTuple)
                self.connection.commit()        #if you do not commit the change  is automatically rolledback
                if (str(isDone).lower() == n):      #the cursor returns the errors found during execution, reterning none if it executed successfuly
                    return isDone
                else:
                    return "false"
        except Error as e:
            return e


    def addBuilding(self,infoTuple):
        try:
            n = 'none'
            cursor = self.connection.cursor()
            query = """
        INSERT INTO agile_project.building VALUES (%s, %s, %s);"""
            with self.connection.cursor() as cursor:
                isDone = cursor.execute(query, infoTuple)
                self.connection.commit()        #if you do not commit the change  is automatically rolledback
                if (str(isDone).lower() == n):      #the cursor returns the errors found during execution, reterning none if it executed successfuly
                    return isDone
                else:
                    return "false"
        except Error as e:
            return e

    def addReservation(self,infoTuple):
        try:
            n = 'none'
            cursor = self.connection.cursor()
            query = """
            INSERT INTO agile_project.reservations(reservation_id,date_of_entry,user_id,floor_id,building_id,room_id,employee_id) VALUES (%s, %s, %s, %s, %s, %s, %s);"""
            with self.connection.cursor() as cursor:
                isDone = cursor.execute(query, infoTuple)
                self.connection.commit()        #if you do not commit the change  is automatically rolledback
                print(isDone)
                if (str(isDone).lower() == n):      #the cursor returns the errors found during execution, reterning none if it executed successfuly
                    return isDone
                else:
                    return "false"
        except Error as e:
            print(e)
            return e

