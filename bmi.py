"""
BMI calculator App Made By Tkinter In Python
"""

# Packages
from tkinter import *
import time
import os

# defining the root window
root = Tk()
root.title('BMI calculator')
root.geometry('400x150')
root.resizable(0,0)
root.config(bg='#121212')


# Functions
def bmi_cal():
    weight = int(weight_entry.get())
    height= int(height_entry.get())/100
    weight_entry.delete(0,END)              
    height_entry.delete(0,END)
    status=''
    bmi = weight/height**2
    if bmi < 18.5:
        status = 'UnderWeight'
    elif bmi <= 24.9 and bmi >= 18.5:
        status = 'Normal Weight'
    elif bmi >= 25 and bmi <= 29.9:
        status='Overweight'
    elif bmi >=30:
        status='Obesity'
    bmi_label = Label(root, text='Your BMI is {} and it means that you have {}'.format(round(bmi,2), status),bg='#121212',fg='white')
    bmi_label.place(relx=0.5, rely=0.7, anchor='c',)
    



# Defining the layout
height_entry = Entry(root,fg='#121212', bg='white')
height_entry.insert(0,'Your Height')
height_val = Label(root, text='cm',bg='#121212', fg='white')

weight_entry = Entry(root,fg='#121212', bg='white')
weight_entry.insert(0,'Your Weight')
weight_val = Label(root, text='kg',bg='#121212', fg='white')

confirm_btn = Button(root, text='What is my BMI ?',bg='#121211', fg='white', command=bmi_cal )

height_entry.grid(row=0, column=0, padx=10,pady=10)
height_val.grid(row=0, column=1, padx=3,pady=10)

weight_entry.grid(row=1, column=0, padx=10,pady=10)
weight_val.grid(row=1, column=1, padx=10,pady=10)

confirm_btn.place(relx=0.7, rely=0.2, anchor='c',)
# Calling the window's main loop
root.mainloop()
