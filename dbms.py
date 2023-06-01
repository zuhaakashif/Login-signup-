import tkinter as tk
import customtkinter
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox
from PIL import Image
import os

app = customtkinter.CTk()
app.title('Login')
app.geometry('450x360')
app.config(bg='#001220')

font1 = ('Helvetica', 25, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold','underline')

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')

def signup():
    username = username_entry.get()
    password = password_entry.get()
    if username!= '' and password != '':
        cursor.execute('SELECT username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None: #retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available.
            messagebox.showerror('Error', 'Username already exists')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt()) #will make password more secure
            #print(hashed_password)
            cursor.execute('INSERT INTO users VALUES (?, ?)', [username, hashed_password])
            conn.commit()
            messagebox.showinfo('Success', 'Account has been created')
    else:
        messagebox.showerror('Error', 'Enter all data')
        
def login_account():
    username = username_entry2.get()
    password = password_entry2.get()
    if username != '' and password != '':
        cursor.execute('SELECT password FROM users WHERE username=?', [username])
        result = cursor.fetchone()
        if result: 
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                messagebox.showinfo('Success', 'Logged in successfully')
            else:
                messagebox.showerror('Error', 'Invalid password')
        else:
            messagebox.showerror('Error', 'Invalid Username')
    else:
        messagebox.showerror('Error', 'Enter all data!')
                   
        
        
def login():
    frame1.destroy()
    frame2 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=470, height=360)
    frame2.place(x=0, y=0)
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
    image = customtkinter.CTkImage(Image.open(os.path.join(path , "1.jpg")), size = (200,400))
    imagef = customtkinter.CTkLabel(frame2, text="", image= image, compound="left")
    imagef.place(x=0, y=0)

    
    login_label2 = customtkinter.CTkLabel(frame2, font=font1, text='Log in',text_color='#fff', bg_color='#001220')
    login_label2.place(x=280, y=20)
    
    
    global username_entry2
    global password_entry2 #using these in another function
    
    username_entry2 = customtkinter.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Username', placeholder_text_color='#a3a3a3', width=200, height=50)
    username_entry2.place(x=230, y=80)
    
    password_entry2 = customtkinter.CTkEntry(frame2, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200, height=50)
    password_entry2.place(x=230, y=150)
    
    login_button2 = customtkinter.CTkButton(frame2, command=login_account, font=font2, text_color='#fff', text='Login', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5,width=120)
    login_button2.place(x=260, y=240)

frame1 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=470, height=360)
frame1.place(x=0, y=0)




signup_label = customtkinter.CTkLabel(frame1, font=font1, text='Sign Up', text_color='#fff', bg_color='#001220' )
signup_label.place(x=280, y=20)

username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fff',fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Username', placeholder_text_color= '#a3a3a3', width=200, height=50)
username_entry.place(x=230, y=80)

password_entry = customtkinter.CTkEntry(frame1, font=font2,show = '*', text_color='#fff',fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Password', placeholder_text_color= '#a3a3a3', width=200, height=50)
password_entry.place(x=230, y=150)

signup_button = customtkinter.CTkButton(frame1, command=signup, font=font2, text_color='#fff', text='Sign Up', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5,width=120)
signup_button.place(x=230, y=220)

login_label = customtkinter.CTkLabel(frame1, font=font3, text='Already have an account?',text_color='#fff', bg_color='#001220')
login_label.place(x=230, y=250)

Login_button = customtkinter.CTkButton(frame1,command=login, font=font4, text_color='#00bf77', text='Login', fg_color='#001220', hover_color='#001220', cursor='hand2',width=40)
Login_button.place(x=270, y=290)

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
image = customtkinter.CTkImage(Image.open(os.path.join(path , "1.jpg")), size = (200,400))
imagef = customtkinter.CTkLabel(frame1, text="", image= image, compound="left")
imagef.place(x=0, y=0)


import sqlite3
con = sqlite3.connect('data.db')
def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM users')
    print(cursorObj.fetchall())
    con.commit()
sql_fetch(con)
app.mainloop()