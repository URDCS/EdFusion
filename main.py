#Python file
import openpyxl as pxl
print('Welcome to EdFusion!')
userId = int(input('Enter your user Id'))
Id = 348

#This is where we will be defining all the functions
def marks():
    Physics = float(input("Enter marks in Physics"))
    Chemistry = float(input("Enter marks in Chemistry"))
    Mathametics = float(input("entter marks in Mathematics"))    
    English = float(input("Enter marks in English"))
    Computer_Science = float(input("enter marks in Computer Science"))
    markslist = [Physics, Chemistry, Mathametics, English, Computer_Science]
    return markslist

#Appending data to an Excel workbook
def appendData(x):
    wb = pxl.Workbook('Data.xlsx')
    wb.create_sheet('Periodic Test - 1')
    wb['Periodic Test - 1'].append(roll, x)
    wb.save()

if userId==348:
    print('Logged in succesfully!')
    roll = int(input('Enter student roll no : '))
    #Function call for input of marks
    appendData(marks())
else:
    print('Invalid credentials')
