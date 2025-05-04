from customtkinter import *

def clicked():
    new = CTk()
    new.geometry('900x500') 
    top = CTkFrame(master=new, width=600, height=200, corner_radius=0, fg_color='#288564')
    top.pack_propagate(False)
    top.pack(side=TOP,fill='x', anchor='n')
    t = CTkLabel(master=top, text='Select Test', text_color='#C4A419')
    t.grid(row=0, column=0, padx=(40,20), pady=(10,10))
    #Creating a dropdown menu
    test_type = CTkOptionMenu(master=top, values=['Periodic Test - 01', 'Periodic Test - 02', 'Mid-Term', 'Periodic Test - 03', 'Preperatory Exam', 'Annual Exam'], fg_color='#8735d4', dropdown_hover_color='#ad0c5a', dropdown_text_color='#e0d799', width=150, height=30)
    test_type.grid(row=0, column=1, pady=(10,10), padx=(20,40))
    #Class and Section
    k = CTkFrame(master=new,width=200, height=200)
    k.pack(side=LEFT, expand=True, pady=(20,20), padx=(20,20), anchor='n')
    klass = CTkLabel(master=k, text='Select the class')
    klass.grid(row=0, column=0, padx=(10,10), pady=(10,10))
    klass_entry = CTkOptionMenu(master=k, values=['1','2','3','4','5','6','7','8','9','10','11','12'])
    klass_entry.grid(row=0, column=1, padx=(10,10), pady=(10,10))
    section = CTkLabel(master=k, text='Select the section')
    section.grid(row=1, column=0, padx=(10,10), pady=(10,10))
    section_entry = CTkOptionMenu(master=k, values=['A', 'B', 'C', 'D'])
    section_entry.grid(row=1, column=1, padx=(10,10), pady=(10,10))
    #Roll Number
    r = CTkFrame(master=new, width=80, height=80)
    r.pack(side=LEFT, expand=True, padx=(5, 5), pady=(20,20), anchor='n')
    roll = CTkLabel(master=r, text='Enter the roll number', anchor='center')
    roll.grid(row=0, column=0, padx=(10,10), pady=(10,10))
    roll_entry = CTkEntry(master=r, width=40, border_color='gray', border_width=2, fg_color='transparent', bg_color='transparent')
    roll_entry.grid(row=1, column=0, padx=(10,10), pady=(10,10))
    #Marks
    m = CTkFrame(master=new,width=200, height=200)
    m.pack(side=LEFT, expand=True, pady=(20,20), padx=(20,10), anchor='n')
    marks = CTkLabel(master=m, text='Enter the marks', anchor='center')
    marks.grid(row=0, column=0, padx=(10,10), pady=(10,10))
    marks_entry = CTkEntry(master=m, border_color='gray', border_width=2, fg_color='transparent', bg_color='transparent')
    marks_entry.grid(row=1, column=0, padx=(10,10), pady=(10,10))
    #Remarks
    rem=CTkFrame(master=new, width=80, height=80)
    rem.pack(side=TOP, padx=(10,10), pady=(20,20), anchor='n')
    remark = CTkLabel(master=rem, text='Enter your remarks(optional)')
    remark.grid(row=0, column=0, padx=(5,5))
    textinput = CTkTextbox(master=rem, width=150, height=60, fg_color='transparent', bg_color='transparent', border_color='gray', border_width=2)
    textinput.grid(row=1, column=0, pady=(0,5))
    def submit():
        class_val = klass_entry.get()
        section_val = section_entry.get()
        test_type_val = test_type.get()
        roll_val = roll_entry.get()
        marks_val = marks_entry.get()
        remarks_val = textinput.get('0.0','end')
        data = [class_val, section_val, test_type_val,  roll_val, marks_val, remarks_val]
        print(data)
    butt = CTkButton(master=new, text='ENTER', corner_radius=50, fg_color='#BD3CD4', hover_color='#4CDB1C', command=submit)
    butt.place(relx=0.5, rely=0.5, anchor='center')
    new.mainloop()

window = CTk()
window.title('EdFusion Login')
window.geometry('400x400')

login = CTkFrame(master=window, fg_color='#203775', width=200, height=200, border_color='#E0E631', border_width=1)
login.pack(expand = True)

welcome = CTkLabel(master=login, text='EdFusion')
welcome.place(relx=0.5, rely=0.1, anchor='center')

text = CTkLabel(master=login, text='Please enter your login ID', bg_color='#203775', text_color='#C4A419')
text.place(relx = 0.5, rely=0.3, anchor='center')

entry = CTkEntry(master=login, bg_color='#203775')
entry.place(relx = 0.5, rely = 0.5, anchor='center')

butt = CTkButton(master=login, text='LOGIN', corner_radius=50, bg_color='#203775', fg_color='#BD3CD4', hover_color='#4CDB1C', command=clicked)
butt.place(relx=0.5, rely=0.8, anchor='center')

window.mainloop()