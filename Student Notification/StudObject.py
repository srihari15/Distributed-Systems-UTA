"""
Name: SRIHARI CHANDRAMOULI
UTA ID: 1001529776
File: server.py
This class will be imported and called in server.py
"""

class StudObject:
    def __init__(self,StudentName,StudentCourse,StudentDecision):       #Initialising the variables using the constructor
        self.Name = StudentName
        self.Course = StudentCourse
        self.Decision = StudentDecision
    def getName(self):              #Getting the name
        return self.Name
    def getCourse(self):            #Getting the course
        return self.Course
    def getDecision(self):          #Getting the decision
        return self.Decision
    def setDecision(self,decision): #Setting the decision
        self.Decision = decision
    def setName(self,name):         #Setting the name
        self.Name = name
    def setCourse(self,course):     #Setting the course
        self.Course = course
