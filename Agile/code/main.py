#THE COMMIT HAS WORKED
#second trial worked
import os
import random
import sys

import mysql
from mysql.connector import connect, Error

sys.path.append(os.path.join('D:/', 'Projects', 'Agile','Agile','code','Model','login'))
from tableClass import logintable
from addTable import addStakeholder
from modifyTable import modifyTable
from reservationTable import reservationTable

def singleton_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kokoHendkokoHend18",
            database="agile_project")
        return connection
    except Error as e:
        print(e)
class main_control:

    _instance = None
    empID = 0
    buildingID = 0
    userInfo = ''
    gender = 'm'
    resID =''


    def __init__(self):
        self.connection = singleton_connection()

    #we override the __new__() method that is called internally by Python when you create an object of a class
    #then check the instances, if an object already exists do not create a new instance, hence singleton
    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(main_control, cls).__new__(cls)
        return cls._instance

    #call model to get building ID
    def getBuildingIDControl(self,id):
        queryobj=modifyTable(self.connection)
        result = queryobj.showEmployee(id)
        self.buildingID = result[0][8]
        return

    #call model to make sure building id exists in db buildings
    def buildingIDCheckControl(self):
        queryobj=reservationTable(self.connection)
        result = queryobj.getBuildingsIDs()
        bds = []
        for item in result:
            bds.append(int(str(item)[1:2]))
        if (self.buildingID not in bds):
            self.buildingID = 1
        return

    def getBID(self):
        return self.buildingID

    def getG(self):
        return self.gender

    def setEligibleNO(self,infotuple):
        queryobj = reservationTable(self.connection)
        queryobj.makeEligibleNo(int(infotuple[2]))
        return

    def decRoom(self,infotuple):
        roomtuple=[]
        roomtuple.append(int(infotuple[5]))
        roomtuple.append(int(infotuple[3]))
        roomtuple.append(int(infotuple[4]))
        queryobj = reservationTable(self.connection)
        queryobj.decreaseRoomAv(roomtuple)
        return

    def confirmRes(self,infotuple):
        queryobj1=reservationTable(self.connection)
        res = queryobj1.genResID()
        infotuple.insert(0,int(str(res[0])[1:2])+1)
        self.resID = infotuple[0]
        result = queryobj1.getAvRooms(infotuple[3],infotuple[4])
        rooms = []
        for item in result:
            rooms.append(int(str(item)[1:2]))
        if len(rooms) == 1 :
            room = rooms[0]
        else:
            room = random.choice(rooms)
        infotuple.append(room)
        infotuple.append(self.empID)
        queryobj= addStakeholder(self.connection)
        result = queryobj.addReservation(infotuple)
        self.setEligibleNO(infotuple)
        self.decRoom(infotuple)
        return result


    def getResInfo(self):
        queryobj=reservationTable(self.connection)
        result = queryobj.showRes(self.resID)
        return result


    # call MODEL to query login info and authenticate info
    def checkloginControl(self,type , usertuple):
        queryobj=logintable(type,self.connection)
        result = queryobj.getloginquery()
        isacceptable=False
        for row in result:
            if (usertuple == row):
                isacceptable = True
                return isacceptable
        return isacceptable

    # call MODEL to query adding info and authenticate insertion
    def addEMployeeControl(self, usertuple):
        queryobj=addStakeholder(self.connection)
        result = queryobj.addEmployee(usertuple)
        return result

    # call MODEL to query adding info and authenticate insertion
    def addBuildingControl(self, usertuple):
        queryobj=addStakeholder(self.connection)
        result = queryobj.addBuilding(usertuple)
        return result

    # call MODEL to query editing info and authenticate update
    def editEMployeeControl(self, usertuple):
        queryobj=modifyTable(self.connection)
        result = queryobj.editEmployee(usertuple)
        return result

    #set building ID for reserving
    def setBID(self,id):
        self.buildingID = id

    #set gender for reserving
    def setG(self,g):
        self.gender = g

    #call model to get gui msgs
    def getGuiMsgsControl(self):
        queryobj=logintable(type,self.connection)
        result = queryobj.gui_msgs()
        return result

    #call model to get employee info
    def getEmplyeeInfoControl(self,id):
        queryobj=modifyTable(self.connection)
        result = queryobj.showEmployee(id)
        return result

    #call model to get user info
    def getUserInfoControl(self,id):
        queryobj=reservationTable(self.connection)
        result = queryobj.showUser(id)
        return result

    #call model to get building info
    def getBuildingInfoControl(self,id):
        queryobj=modifyTable(self.connection)
        result = queryobj.showBuilding(id)
        return result

    #call model to get building info
    def getBuildingRControl(self):
        queryobj=reservationTable(self.connection)
        result = queryobj.showBuilding(self.buildingID)
        return result

    def getAvBedsControl(self):
        queryobj=reservationTable(self.connection)
        result = queryobj.getAvBeds(self.buildingID)
        if (str(result[0])[1:5].lower() == 'none'):
            return 0
        return result


    def incrementBuildingID(self):
        self.buildingID =  self.buildingID + 1


    # call MODEL to query editing info and authenticate update
    def editBuildingControl(self, usertuple):
        queryobj=modifyTable(self.connection)
        result = queryobj.editBuilding(usertuple)
        return result


    def getResFloorsControl(self):
        queryobj=reservationTable(self.connection)
        result = queryobj.getResFloors(self.buildingID,self.gender)
        return result

    def getAvBedsResControl(self,id):
        queryobj=reservationTable(self.connection)
        result = queryobj.getAvFloorBeds(self.buildingID,id)
        return