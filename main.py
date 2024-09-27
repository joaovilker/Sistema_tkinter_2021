from customtkinter import *
from tkinter import ttk, messagebox
import sqlite3
from Intro import Splash
from Userlogin import Login
from User_menu import User
from PIL import Image

b = 0

class Main(Splash, Login, User):
    def __init__(self):
        global b
        if b == 0:
            Splash.__init__(self)  # Inicialize Splash primeiro
            super().__init__()     # Depois, inicialize Login e User
            b = 1
        else:
            print("b já foi definido como 1")


        Login.__init__(self)
        self.loginw.mainloop()
        self.loginw.withdraw()
        self.account_type = 'GUEST'
        self.mainw = CTkToplevel()
        width = 1386
        height = 780
        self.mainw.iconbitmap(r'.\images\icon.ico')
        screen_width = self.mainw.winfo_screenwidth()
        screen_height = self.mainw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.mainw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.mainw.title("SISTEMA DE VENDAS EM TKINTER")
        self.mainw.resizable(0, 0)
        self.mainw.protocol('WM_DELETE_WINDOW', self.__Main_del__)

        self.getdetails()

    def __Main_del__(self):
        if messagebox.askyesno("SAIR", "Você está de acordo em fechar o programa?"):
            self.loginw.quit()
            self.mainw.quit()
            exit(0)

    def getdetails(self):
        self.buildmain()

    def buildmain(self):
        if self.account_type == 'ADMIN':
            pass 
        else:
            User.__init__(self, self.mainw)
            self.user_mainmenu(8, 8)
            self.mainw.iconbitmap(r'.\images\icon.ico')
            self.logout.configure(command=self.__Main_del__)

            self.topframe = CTkFrame(self.mainw, width=1800, height=120, fg_color="#8A2BE2")
            self.topframe.place(x=0, y=0)

            self.storelable = CTkLabel(self.topframe, text="REISA Outlet", fg_color="#8A2BE2", justify="center", font=("Roboto", 30, "bold"), text_color="snow")
            self.storelable.place(x=360, y=30)

            mi = CTkImage(dark_image=Image.open("images/perfil1.png").resize((100, 100)))
            self.myprofile = CTkLabel(self.topframe, text=(self.username.get()).capitalize(), image=mi)
            self.myprofile.place(x=1300, y=15)



if __name__ == "__main__":
    app = Main()
    b = 0
    root = CTk()
    w = Main()
    w.mainw.mainloop()