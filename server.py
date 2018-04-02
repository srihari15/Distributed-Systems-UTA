"""
Name: SRIHARI CHANDRAMOULI
UTA ID: 1001529776
File: server.py
"""
import sqlite3
import Pyro4
from StudObject import StudObject

file = 'New.sqlite'  #Name of the file
mytable = 'New1'     #Name of the table
type = 'VARCHAR'     #Type of the data
MQList = []          #The Message queue List (Data Structure)

@Pyro4.expose        #Starting the remote calling
@Pyro4.behavior(instance_mode="single")
class MQObject(object):
    def __init__(self):
        print("starting")
        self.curso = sqlite3.connect(file)    #The connection is established with the sqlite file
        self.PopulateData()


    def PopulateData(self):                    #This function is used to append the values in the database as well as in the list
        self.cursor1 = sqlite3.connect(file)
        cursor = self.curso.cursor()
        data = cursor.execute("SELECT * FROM " + mytable).fetchall()      #Fetching all the contents from the table
        cursor.execute("SELECT * FROM " + mytable)
        if (data.__sizeof__() > 0):
            for rows in cursor:
                MQList.append(StudObject(rows[0], rows[1], rows[2]))   #Pushing the data in the list
        else:
            return

    def DELData(self,value1,value2,value3):       #This method pops out data that has been used, from the list as well as the database
        print("Delete Function")
        self.DatabaseConnection = sqlite3.connect(file)
        cursor = self.DatabaseConnection.cursor()
        cursor.execute("DELETE FROM "+mytable+" WHERE Name = (?) AND Course = (?) AND Status = (?)",(value1,value2,value3))   #The SQL command for the Deletetion of the elements in the table
        self.DatabaseConnection.commit()
        for rows in cursor:
            print(rows[1])
        self.DatabaseConnection.close()
        for i in range(0, len(MQList)):   #iterating through the list and popping the elements inside the list
            Tem = MQList.pop(i)
            print(Tem.getName())
            if (Tem.getName() == value1):       #Here we are specifying which column
                if (Tem.getCourse() == value2):
                    return
                else:
                    MQList.insert(i,Tem)
            else:
                MQList.insert(i, Tem)

    def Seek_Data(self,fix,CesName):       #This function lets us peek or see what has happened before in the previous processes such that the next process can find it useful by peeking
        self.DatabaseConnection = sqlite3.connect(file)
        cursor = self.DatabaseConnection.cursor()
        cursor.execute("SELECT * FROM "+mytable+" WHERE Status = (?)",(CesName,))
        for rows in cursor:
            self.DatabaseConnection.close()
            return rows
        return None

    def InsertinQueue(self,value1,value2,value3):         #This method will push the name, course and status inside the queue
        print("Inside")
        self.DatabaseConnection = sqlite3.connect(file)
        cursor = self.DatabaseConnection.cursor()
        type = "VARCHAR"
        cursor.execute("INSERT INTO "+mytable+" VALUES (?,?,?)",(value1,value2,value3))  #SQL command for inserting values
        self.DatabaseConnection.commit()
        self.DatabaseConnection.close()
        tempObject = StudObject(value1,value2,value3)
        MQList.append(tempObject)
        print(len(MQList))

"""
Starting the Remote calls 
with the help of Pyro4
"""
s = MQObject()              #instantiating the class
daemon = Pyro4.Daemon(None, 1511,None)
uri = daemon.register(MQObject,"hari.com")
print(uri)
daemon.requestLoop()

