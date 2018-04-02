"""
Name: SRIHARI CHANDRAMOULI
UTA ID: 1001529776
File: student.py
"""
import Pyro4

uri = "PYRO:hari.com@localhost:1511"          #The URI that is fetched when calling the server
remote_procedure_call = Pyro4.Proxy(uri)                        #It willl check whether the uri is true or not
while True:                                   #If it is true, we will enter the name,course and push it to the queue by calling the InsertinQueue() remotely
    name = input("Enter your name : ")
    course = input("Enter your course : ")
    remote_procedure_call.InsertinQueue(name,course,"NONE")       #Since there are 3 columns, we need to give NONE if we do not want to change that particular column

