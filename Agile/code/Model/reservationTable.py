from getpass import getpass
from mysql.connector import connect, Error


# This is a class for editing employees and buildings into the db
class reservationTable:
    def __init__(self,connection):
        self.connection=connection

    def showUser(self,id):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT * 
            FROM agile_project.user
            WHERE national_id = {} ;""".format(id)
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(e)
            return e

    def showRes(self,id):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT * 
            FROM agile_project.reservations
            WHERE reservation_id = {} ;""".format(id)
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(e)
            return e

    def makeEligibleNo(self,id):
        try:
            n= 'none'
            cursor = self.connection.cursor()
            query = """
            UPDATE agile_project.user 
            SET eligible = 'n'
            WHERE national_id = {} ;""".format(id)
            with self.connection.cursor() as cursor:
                isDone = cursor.execute(query)
                self.connection.commit()  # if you do not commit the change  is automatically rolledback
                if (
                        str(isDone).lower() == n):  # the cursor returns the errors found during execution, reterning none if it executed successfuly
                    return isDone
                else:
                    return "false"
        except Error as e:
            print(e)
            return e

    def decreaseRoomAv(self,infotuple):
        try:
            n = 'none'
            cursor = self.connection.cursor()
            query = """
            UPDATE agile_project.room 
            SET 
                available_beds = available_beds - 1
            WHERE
                room_id = %s AND floor_id = %s
                    AND building_id = %s;"""
            with self.connection.cursor() as cursor:
                isDone = cursor.execute(query,infotuple)
                self.connection.commit()        #if you do not commit the change  is automatically rolledback
                if (str(isDone).lower() == n):      #the cursor returns the errors found during execution, reterning none if it executed successfuly
                    return isDone
                else:
                    return "false"
        except Error as e:
            print(e)
            return e


    def genResID(self):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT Max(reservation_id) 
            FROM agile_project.reservations;"""
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
                return result
        except Error as e:
            print(e)
            return e

    def getAvBeds(self,id):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT SUM(available_beds) 
            FROM agile_project.room 
            WHERE building_id = {};""".format(id)
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(e)
            return e

    def getAvRooms(self,fid,bid):
        try:
            rtuple =[]
            rtuple.append(fid)
            rtuple.append(bid)
            cursor = self.connection.cursor()
            query = """
            SELECT room_id 
            FROM agile_project.room 
            WHERE floor_id = %s AND building_id= %s AND available_beds>0;"""
            with self.connection.cursor() as cursor:
                cursor.execute(query,rtuple)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(e)
            return e


    def getResFloors(self,id,g):
        try:
            infotuple = []
            infotuple.append(g)
            infotuple.append(id)
            infotuple.append(id)
            cursor = self.connection.cursor()
            query =  """
            SELECT floor_id 
            FROM agile_project.floor 
            WHERE gender = %s and building_id = %s and             
            floor_id in (SELECT	floor_id 
            FROM agile_project.room 
            WHERE building_id = %s
            GROUP BY floor_id
            HAVING	 SUM(available_beds) > 0)"""
            with self.connection.cursor() as cursor:
                cursor.execute(query,infotuple)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(e)
            return e

    def getAvFloorBeds(self,bid,fid):
        try:
            infotuple = []
            infotuple.append(bid)
            infotuple.append(fid)
            cursor = self.connection.cursor()
            query = """
            SELECT SUM(available_beds)
            FROM agile_project.room
            WHERE building_id = %s and floor_id = %s
            GROUP BY floor_id
            HAVING SUM(available_beds) > 0;"""
            with self.connection.cursor() as cursor:
                cursor.execute(query,infotuple)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(e)
            return e

    def showBuilding(self, id):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT building_id , location 
            FROM agile_project.building
            WHERE building_id = {} ;""".format(id)
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(e)
            return e


    def getBuildingsIDs(self):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT building_id 
            FROM agile_project.building
            ;""".format(id)
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()

                return result
        except Error as e:
            print(e)
            return e


