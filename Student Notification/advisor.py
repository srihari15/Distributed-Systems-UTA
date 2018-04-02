"""
Name: SRIHARI CHANDRAMOULI
UTA ID: 1001529776
File: advisor.py
"""

import Pyro4
import time as t    #time as instance t
import random

uri = "PYRO:hari.com@localhost:1511"       #Again the uri when running the server
remote_procedure_call = Pyro4.Proxy(uri)                      #Checking if it is correct or not
while 1==1:
    dlist = remote_procedure_call.Seek_Data("Advisor","NONE")      #Check whether there is any data for the advisor to make an advise
    if dlist != None:
        remote_procedure_call.DELData(dlist[0], dlist[1], dlist[2])   #If there is no data as such, just pop the data
        randdd = random.randint(1,10)               #Randomise the decision
        if (randdd % 2 == 0):                       #If it is even, will prin APPROVED else NOT APPROVED
            MutatedList = [dlist[0], dlist[1], "APPROVED"]
        else:
            MutatedList = [dlist[0], dlist[1], "NOT APPROVED"]
        print(MutatedList[0] + " "+MutatedList[1]+ " "+MutatedList[2]+"\n")
        remote_procedure_call.InsertinQueue(MutatedList[0], MutatedList[1], MutatedList[2])  #Pushing the values to the queue
    else:
        print("No message found")
        t.sleep(3)   #Giving 3 seconds of time to read data
