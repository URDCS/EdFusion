from customtkinter import *

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