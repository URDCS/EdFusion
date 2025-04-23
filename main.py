#Python file
import csv
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

if userId==348:
    print('Logged in succesfully!')
    roll = int(input('Enter student roll no : '))
    #Function call for input of marks
    print(marks())
else:
    print('Invalid credentials')
