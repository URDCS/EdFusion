#Python file
import openpyxl as pxl
import tkinter as tk

print('Welcome to EdFusion!')
#userId = int(input('Enter your user Id'))
Id = 348
'''
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
'''
#Defining a function to redirect to entry page
def submit():
    entry_window = tk.Tk()
    entry_window.title('EdFusion Entry')
    entry_window.config(width=entry_window.winfo_width)
    entry_window.config(height=entry_window.winfo_height)
    entry_window.config(background='#000000')
    #Creating Labels
    roll = tk.Label(entry_window, text='Enter the roll number of the student', font=('Ariel',25,'bold'), foreground='#4993BB', background='#000000')
    roll.grid(row=0, column=0)
    roll_input = tk.Entry(entry_window, foreground='#000000', font=('Ariel',25,'bold'))
    roll_input.grid(row=0, column=1)
    #Creating button
    mark_entry_button = tk.Button(entry_window, text='Submit', font=('Ariel',25,'bold'), background='#FFA500')
    mark_entry_button.grid(row=1,column=0)
    window.destroy()
    entry_window.mainloop()

#Creating a window object and setting window geometry
window = tk.Tk()
window.title('EdFusion Login')

window.geometry(window.wm_geometry)
window.config(background='#000000')

#Creating Labels and Entries
login = tk.Label(window, text='Enter your login ID', background='#000000', font=('Ariel',25,'bold'), fg='#4993BB')
login.grid(row=0, column=0)
login_input = tk.Entry(window, foreground='#000000', font=('Ariel',25,'bold'))
login_input.grid(row=0, column=1)

login_button = tk.Button(window, text='LOGIN', font=('Ariel',25,'bold'), background='#FFA500', command=submit)
login_button.grid(row=5, column=0)



window.mainloop()
