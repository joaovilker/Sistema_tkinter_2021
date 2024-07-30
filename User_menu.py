
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from adicionais import mycombobox




class User:
    def __init__(self,mainw):
        self.mainw=mainw

    def user_mainmenu(self,a,b):
        self.mainw.iconbitmap(r'C:\Sistema_vendas_tkinter_copia\images\icon.ico')
        self.mainframe = LabelFrame(self.mainw, width=800, height=140, bg="#f7f7f7")
        self.mainframe.place(x=330, y=120)
        mi = PhotoImage(file="images/carrinho.png")
        mi = mi.subsample(a, b)
        self.aitems = Button(self.mainframe, text="ITEMS",bd=0,font="roboto 11 bold", image=mi)
        self.aitems.image = mi
        self.aitems.place(x=260, y=17)
        mi = PhotoImage(file="images/nota.png")
        mi = mi.subsample(a,b)
        self.aitems = Button(self.mainframe, text="NOTAS",bd=0,font="roboto 11 bold", image=mi)
        self.aitems.image = mi
        self.aitems.place(x=62, y=17)
        mi = PhotoImage(file="images/usertrocar.png")
        mi = mi.subsample(a, b)
        self.changeuser = Button(self.mainframe, text="SAIR",bd=0,font="roboto 11 bold", image=mi)
        self.changeuser.image = mi
        self.changeuser.place(x=460, y=17)
        mi = PhotoImage(file="images/sair.png")
        mi = mi.subsample(a, b)
        self.logout = Button(self.mainframe, text="FECHAR",bd=0,font="roboto 11 bold", image=mi)
        self.logout.image = mi
        self.logout.place(x=670, y=17)
        self.tableframe1 =Frame(self.mainw, width=150, height=400,bg="#9ACD32")
        self.tableframe1.place(x=1230, y=270, anchor=NE)
        self.tableframe1info=self.tableframe1.place_info()
        self.tableframe =Frame(self.mainw, width=350, height=700,bg="#9ACD32")
        self.tableframe.place(x=1110, y=300, anchor=NE)
        self.tableframeinfo = self.tableframe.place_info()
        self.entryframe = Frame(self.mainw, width=800, height=350, bg="#9ACD32")
        self.entryframe.place(x=810, y=460+20)
        self.entryframeinfo = self.entryframe.place_info()
        self.entryframe1 = Frame(self.mainw, width=500, height=350, bg="#9ACD32")
        self.entryframe1.place(x=230, y=470+20)
        self.entryframe1info=self.entryframe1.place_info()


    def builditemtable(self):
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe.place(self.tableframeinfo)
        self.tableframe1.place_forget()
        scrollbarx = Scrollbar(self.tableframe, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe, orient=VERTICAL)
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
        self.tree.heading('Description', text="Descricao", anchor=W)
        self.tree.heading('Category', text="Categoria", anchor=W)
        self.tree.heading('Price', text="Preco", anchor=W)
        self.tree.heading('Stocks', text="Estoque", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
      

    def make_invoice(self):

        self.tableframe.place_forget()
        self.entryframe.place(self.entryframeinfo)
        self.entryframe1.place(self.entryframe1info)
        self.tableframe1.place(self.tableframe1info)
        scrollbarx = Scrollbar(self.tableframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe1, columns=("Transaction ID", "Product ID", "Product Name",
        'Quantity', 'Price','Date','Time'), selectmode="browse", height=6,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=140)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=170)
        self.tree.column('#4', stretch=NO, minwidth=0, width=130)
        self.tree.column('#5', stretch=NO, minwidth=0, width=130)
        self.tree.column('#6', stretch=NO, minwidth=0, width=130)
        self.tree.column('#7', stretch=NO, minwidth=0, width=130)
        self.tree.heading('Transaction ID', text="Transacao", anchor=W)
        self.tree.heading('Product ID', text="Produto ID", anchor=W)
        self.tree.heading('Product Name', text="Produto Nome", anchor=W)
        self.tree.heading('Quantity', text="Quantidade", anchor=W)
        self.tree.heading('Price', text="Preco", anchor=W)
        self.tree.heading('Date', text="Data", anchor=W)
        self.tree.heading('Time', text="Hora", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.tree.bind("<<TreeviewSelect>>")

        self.user_input()


    def user_input(self):

        self.cur.execute('')
        
        self.qty = StringVar(value=1)
        self.additem=StringVar()
        self.total=IntVar(value=0)
        Button(self.entryframe,text="Efetuar",bd=1,width=8,height=7,bg="#9ACD32",font="roboto 10").place(x=0,y=30)
        Button(self.entryframe, text="Add Carrinho", bd=1, width=10, height=3,bg="#9ACD32",font="roboto 10").place(x=100,y=80)
        Button(self.entryframe, text="Remover", bd=1, width=10, height=3, bg="#9ACD32",font="roboto 10").place(x=210, y=80)
        entercart=mycombobox(self.entryframe,width=20,textvariable=self.additem,font="roboto 12")
        entercart.place(x=100,y=30,height=30)
        cartqty = Entry(self.entryframe,textvariable=self.qty,width=9,bg="#FFFFFF",font="roboto 12")
        cartqty.place(x=320,y=30,height=30)
        carttotal = Entry(self.entryframe, textvariable=self.total, width=20, state='readonly', bg="#FFFFFF", font="roboto 12")
        carttotal.place(x=130, y=185, height=60)
        Label(self.entryframe, text="Quantidade", font="roboto 12 bold", bg="#9ACD32").place(x=318,y=0)
        Label(self.entryframe, text="Pesquisar", font="roboto 12 bold", bg="#9ACD32").place(x=100, y=0)
        Label(self.entryframe, text="Valor Pagar", font="roboto 14 bold", bg="#9ACD32").place(x=0, y=205)
        self.cur.execute("")
       
        Label(self.tableframe1, text="N_Cupon. ", font="roboto 14 bold", bg="#9ACD32").grid(row=0, column=0)
       
        va=0
        va += 65
        
        Entry(self.entryframe1,  font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162, y=0,height = 40)
        Entry(self.entryframe1, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162, y=65,height=40)
        Entry(self.entryframe1, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162,y=65*2,height=40)
        Entry(self.entryframe1, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162,y=65*3,height=40)
        self.id_qty=dict()
        self.cur.execute("")
