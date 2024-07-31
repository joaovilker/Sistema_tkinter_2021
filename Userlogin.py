import customtkinter
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class Login:

    def __init__(self):
        self.loginw=Tk()
        
        self.loginw.title("Login")
        width = 500
        height = 600
        self.loginw.iconbitmap(r'C:\Users\joaov\Documents\Sistema_tkinter_2021\images\icon.ico')
        screen_width = self.loginw.winfo_screenwidth()
        screen_height = self.loginw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.loginw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.loginw.resizable(0, 0)
        self.loginw.protocol('WM_DELETE_WINDOW', self.__login_del__)
        self.loginw.config(bg="#1F5673")
       
        self.logintable()
        self.username = StringVar(value="Username")
        self.password = StringVar(value="Password")
        self.obj()

    def __login_del__(self):
        if messagebox.askyesno("SAIR", "Você está de acordo em fechar o programa?") == True:
            self.loginw.destroy()
            exit(0)

    def logintable(self):
        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(20) PRIMARY KEY,
                password VARCHAR(20) NOT NULL,
                account_type VARCHAR(10) NOT NULL
            );
        """)
        self.base.commit()
  

    def obj(self):
        self.loginframe=LabelFrame(self.loginw,bg="#1F5673",height=400,width=300)
        self.loginw.bind('<Return>')
        self.loginframe.place(x=103,y=95)
        self.toplabel = Label(self.loginframe, fg="white", bg="#1F5673", anchor="center", text="Login", font="Roboto 40 bold")
        self.toplabel.place(x=75,y=25)
        self.us = ttk.Entry(self.loginframe, width=20, textvariable=self.username,font="Roboto 14 ")
        self.us.place(x=35,y=145,height=40)
        self.pa = ttk.Entry(self.loginframe, width=20, textvariable=self.password,font="Roboto 14 ")
        self.pa.place(x=35,y=185,height=40)
        self.us.bind('<Button-1>', self.onclick)
        self.pa.bind('<Button-1>', self.onclick1)
        self.signin = Button(self.loginframe,width=20, text="ENTRAR",bg="#008B8B",fg="white",bd="0",command=self.checkuser,font="Roboto 14")
        self.signin.place(x=35,y=290)

    def checkuser(self):
        if not hasattr(self, 'cur'):
            print("Database cursor is not initialized")
            return

        s = self.username.get().upper()
        s1 = self.password.get().upper()
        self.cur.execute("SELECT * FROM users WHERE username=? AND password=?", (s, s1))
        l = self.cur.fetchall()
        if len(l) > 0:
            self.success()
        else:
            self.fail()

    def success(self):
        messagebox.showinfo("Success","Login successful")
        self.loginw.quit()
    
    
    def fail(self):
        messagebox.showerror("ATENCAO","USUARIO OU SENHA INCORRETAS")

    

    def onclick(self,event):
       
            self.us.delete(0, "end")

    def onclick1(self,event):
       
            self.pa.delete(0, "end")
            self.pa.config(show = "*")

