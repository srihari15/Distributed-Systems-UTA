"""
Name: SRIHARI CHANDRAMOULI
UTA ID: 1001529776
File: notification.py
"""
import Pyro4
import time

uri = "PYRO:hari.com@localhost:1511"    #Again the uri when running the server
remote_procedure_call = Pyro4.Proxy(uri)                  #Checking if it is correct or not!
while True:
    rows = remote_procedure_call.Seek_Data("NOTIFICATION", "APPROVED")     #If correct, check whether there is a value like APPROVED or NOT APPROVED
    ro = remote_procedure_call.Seek_Data("NOTIFICATION","NOT APPROVED")
    if rows != None or ro != None:
        if rows != None:
            remote_procedure_call.DELData(rows[0], rows[1], rows[2])   #Keep popping the elements from the list as we print them
            print(rows[0]+" "+rows[1]+" "+rows[2])
        if ro != None:
            remote_procedure_call.DELData(ro[0], ro[1], ro[2])        #The same thing as above
            print(ro[0]+" "+ro[1]+" "+ro[2])
    else:
        print("No message found!")
        time.sleep(7)                           #Giving it 7 seconds to read the data

