from tkinter import Label, Tk
from PIL import ImageTk, Image


class Splash:
    def __init__(self):
        self.root = Tk()
        self.root.title("Splash Screen")
        self.img = Image.open(r".\icons\images.png")
        self.tk_img = ImageTk.PhotoImage(self.img)

        fotoframe = Label(self.root, image=self.tk_img)
        fotoframe.pack()
        self.root.mainloop()

        self.splashmainw.config(bg="#1F5673")
        tela_largura = self.splashmainw.winfo_screenwidth()
        tela_altura = self.splashmainw.winfo_screenheight()
        x = (tela_largura / 2 ) - (width /2 )
        y = (tela_altura / 2 ) - (height /2 )
        self.splashmainw.geometry("%dx%d+%d+%d" % (width,height,x,y))
        self.splashmainw.resizable(0,0)
        path = "images/intro.jpg"
        self.img = ImageTk.PhotoImage(Image.open(path))  # Armazenando a imagem na instância
        main = LabelFrame(self.splashmainw, width=890, height=560, bg="#1F5673", relief="sunken", bd="0")
        main.place(x=55, y=70)
        fotoframe = LabelFrame(main, width=420, height=444, bg="#1F5673", relief="raised", bd="0")
        foto = Label(fotoframe, image=self.img)
        foto.place(x=6, y=6)
        fotoframe.place(x=10, y=100)

        Label(main, text="SISTEMA DE VENDAS", font="roboto 28 bold underline", bg="lightblue").place(x=45, y=10)
        Label(main, text="João Vilker", font="roboto 32 bold", bg="lightblue").place(x=450, y=160)
        Label(main, text="Programador", font="roboto 16 bold", bg="lightblue").place(x=445+5, y=260)
        Label(main, text="Desenvolvedor", font="roboto 16 bold", bg="lightblue").place(x=450, y=310)
        Label(main, text="Email : joao.vilker@hotmail.com", font="roboto 16 bold", bg="lightblue").place(x=445+5, y=360)
        Label(main, text="Telefone : (+55 11 91852-0654)", font="roboto 16 bold", bg="lightblue").place(x=445+5, y=410)
        self.splashmainw.after(1000, lambda: self.splashmainw.destroy())

        self.splashmainw.mainloop()
