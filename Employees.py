"""
     
    Employees.py: Program is written using functions to re-write the Employess file,
                  Submitted By : Jasneet Kaur
                                 (c0750018)
"""
import csv
from datetime import datetime as dt
f = open('Employee.txt', "w")   # File(Employees.txt) is opened for writing
f.write(" Employee Salary Estimates\n")
f.write("----------------------------\n\n\n")

f.write('{:^15} {:^15} {:^15} {:^15} {}'.format("Employee Name", "Hire date", "Old rate", "New rate",'\n'))
f.write("-----------------------------------------------------------------------\n")

def reformatFile(x):   #Function to re-format  the file(Employees.txt)
    f.write('{:<25} {: %m-%d-%Y} {:^24} {:.2f} {} '.format(x[1]+" "+x[2],dt.strptime(x[3],' %Y-%m-%d') ,x[4],(1.0385 * float(x[4])),'\n')) 

with open('Employees.csv', "r") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        if row[4]=="contract_rate":
            continue
        else:
            reformatFile(row)
f.close()               #Close the file

    
