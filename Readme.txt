Name : SRIHARI CHANDRAMOULI
UTA ID : 1001529776
Net id : sxc9776
Date : 5th November 2017
Programming Language: PYTHON
Version: 3.6

CODE STRUCTURE
**************
Server: server.py
******
Client: student.py, advisor.py, notification.py
******
I have used a sqlite3 database: New.sqlite		

THINGS TO REMEMBER BEFORE EXECUTION
************************************
	 We have used the RPC concept in Python. So install Pyro4 before the execution of the project
EXECUTION
*********
1) First, run the server.py 
2) Then run the student.py, advisor.py and notification.py	
3) All the 4 python files will run simultaneously.
4) In the student process, enter the student name and the course.
5) The name and the course will be outputted to the advisor process and the notification process.
6) The advisor process will advise randomly whether or not the subject is recommended and based on that, its APPROVED OR NOT APPROVED.
7) Notification process will print all the information and simutaneously delete the values from the list and the table.
8) Use the .sh file created for the .py files in order to execute it.
9) The StudObject.py file will not be called independently since it will be imported to the server.py

Citation
*********
   1) Name :  sebastianraschka      
       Availablity : http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
   2) Name :  snakecharmerb
       Availablity : https://stackoverflow.com/questions/36439032/how-do-you-pass-through-a-python-variable-into-sqlite3-query
   3) Name :  Abhijit
       Availability: https://stackoverflow.com/questions/10139866/calling-variable-defined-inside-one-function-from-another-function

