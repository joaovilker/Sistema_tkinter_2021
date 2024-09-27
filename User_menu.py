from customtkinter import *
from PIL import Image 
import sqlite3
from tkinter import Entry, ttk  # Certifique-se de importar ttk para usar Treeview
from tkinter import Scrollbar, HORIZONTAL, VERTICAL
from adicionais import mycombobox
from customtkinter import CTkScrollbar



class User:
    def __init__(self, mainw):
        self.mainw = mainw
        self.setup_ui()

    def setup_ui(self):
        self.mainw.iconbitmap(r'.\images\icon.ico')
        self.mainframe = CTkFrame(self.mainw, width=800, height=140, fg_color="#f7f7f7")
        self.mainframe.place(x=330, y=120)

        mi = Image.open("images/carrinho.png").resize((30, 30))
        mi = CTkImage(dark_image=mi)
        self.aitems = CTkButton(self.mainframe, text="ITEMS", font=("Roboto", 11, "bold"), image=mi, fg_color="#f7f7f7", command=self.builditemtable)
        self.aitems.place(x=260, y=17)

        mi = Image.open("images/nota.png").resize((30, 30))
        mi = CTkImage(dark_image=mi)
        self.anotas = CTkButton(self.mainframe, text="NOTAS", font=("Roboto", 11, "bold"), image=mi, fg_color="#f7f7f7", command=self.make_invoice)
        self.anotas.place(x=62, y=17)

        mi = Image.open("images/usertrocar.png").resize((30, 30))
        mi = CTkImage(dark_image=mi)
        self.changeuser = CTkButton(self.mainframe, text="SAIR", font=("Roboto", 11, "bold"), image=mi, fg_color="#f7f7f7")
        self.changeuser.place(x=460, y=17)

        mi = Image.open("images/sair.png").resize((30, 30))
        mi = CTkImage(dark_image=mi)
        self.logout = CTkButton(self.mainframe, text="FECHAR", font=("Roboto", 11, "bold"), image=mi, fg_color="#f7f7f7")
        self.logout.place(x=670, y=17)
        self.logout.configure(command=self.__Main_del__)

        self.tableframe1 = CTkFrame(self.mainw, width=150, height=400, fg_color="#9ACD32")
        self.tableframe1.place(x=1230, y=270, anchor=NE)
        self.tableframe = CTkFrame(self.mainw, width=350, height=700, fg_color="#9ACD32")
        self.tableframe.place(x=1110, y=300, anchor=NE)
        self.entryframe = CTkFrame(self.mainw, width=800, height=350, fg_color="#9ACD32")
        self.entryframe.place(x=810, y=480)
        self.entryframe1 = CTkFrame(self.mainw, width=500, height=350, fg_color="#9ACD32")
        self.entryframe1.place(x=230, y=490)

    def __Main_del__(self):
        # Fecha a aplicação ou executa outra ação desejada
        print("Botão 'FECHAR' clicado")
        self.mainw.destroy()  # Fecha a janela principal

    def builditemtable(self):
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe1.place_forget()  # Ocultar o frame adicional, se necessário
        self.tableframe.place(relx=0.5, rely=0.5, anchor=CENTER)  # Posicionar o frame principal

        scrollbarx = CTkScrollbar(self.tableframe, orientation=HORIZONTAL)
        scrollbary = CTkScrollbar(self.tableframe, orientation=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe, columns=("Product ID", "Product Name", "Description", "Category",
                                                        'Price', 'Stocks'), selectmode="extended", height=18,
                                yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)
        self.tree.heading('Product ID', text="Produto ID", anchor=W)
        self.tree.heading('Product Name', text="Produto Nome", anchor=W)
        self.tree.heading('Description', text="Descrição", anchor=W)
        self.tree.heading('Category', text="Categoria", anchor=W)
        self.tree.heading('Price', text="Preço", anchor=W)
        self.tree.heading('Stocks', text="Estoque", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.configure(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        scrollbary.configure(command=self.tree.yview)

    def make_invoice(self):
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe1.place_forget()
        self.tableframe.place(relx=0.5, rely=0.5, anchor=CENTER)
        scrollbarx = CTkScrollbar(self.tableframe, orientation=HORIZONTAL)
        scrollbary = CTkScrollbar(self.tableframe, orientation=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe, columns=("Product ID", "Product Name", "Description", "Category",'Price', 'Stocks'), selectmode="extended", height=18, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)
        self.tree.heading('Product ID', text="Produto ID", anchor=W)
        self.tree.heading('Product Name', text="Produto Nome", anchor=W)
        self.tree.heading('Description', text="Descrição", anchor=W)
        self.tree.heading('Category', text="Categoria", anchor=W)
        self.tree.heading('Price', text="Preço", anchor=W)
        self.tree.heading('Stocks', text="Estoque", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.configure(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        scrollbary.configure(command=self.tree.yview)

    def user_input(self):
        self.qty = IntVar()
        self.qty.set(1)
        self.additem = StringVar()
        self.total = IntVar(value=0)

        CTkButton(self.entryframe, text="Efetuar", width=8, height=7, fg_color="#9ACD32", font=("Roboto", 10)).place(x=0, y=30)
        CTkButton(self.entryframe, text="Add Carrinho", width=10, height=3, fg_color="#9ACD32", font=("Roboto", 10)).place(x=100, y=80)
        CTkButton(self.entryframe, text="Remover", width=10, height=3, fg_color="#9ACD32", font=("Roboto", 10)).place(x=210, y=80)

        entercart = mycombobox(self.entryframe, width=20, textvariable=self.additem, font=("Roboto", 12))
        entercart.place(x=100, y=30, height=30)

        cartqty = CTkEntry(self.entryframe, textvariable=self.qty, width=9, fg_color="#FFFFFF", font=("Roboto", 12))
        cartqty.place(x=320, y=30, height=30)

        carttotal = CTkEntry(self.entryframe, textvariable=self.total, width=20, state='readonly', fg_color="#FFFFFF", font=("Roboto", 12))
        carttotal.place(x=130, y=185, height=60)

        CTkLabel(self.entryframe, text="Quantidade", font=("Roboto", 12, "bold"), fg_color="#9ACD32").place(x=318, y=0)
        CTkLabel(self.entryframe, text="Pesquisar", font=("Roboto", 12, "bold"), fg_color="#9ACD32").place(x=100, y=0)
        CTkLabel(self.entryframe, text="Valor Pagar", font=("Roboto", 14, "bold"), fg_color="#9ACD32").place(x=0, y=205)

        CTkLabel(self.tableframe1, text="N_Cupon. ", font=("Roboto", 14, "bold"), fg_color="#9ACD32").grid(row=0, column=0)

        Entry(self.entryframe1, font=("Roboto", 14), bg="#FFFFFF", width=25, state='readonly').place(x=162, y=0, height=40)
        Entry(self.entryframe1, font=("Roboto", 14), bg="#FFFFFF", width=25, state='readonly').place(x=162, y=65, height=40)
        Entry(self.entryframe1, font=("Roboto", 14), bg="#FFFFFF", width=25, state='readonly').place(x=162, y=130, height=40)
        Entry(self.entryframe1, font=("Roboto", 14), bg="#FFFFFF", width=25, state='readonly').place(x=162, y=195, height=40)
        self.id_qty = dict()


if __name__ == "__main__":
    root = CTk()
    app = User(root)
    app.user_mainmenu(1, 1)
    root.mainloop()
