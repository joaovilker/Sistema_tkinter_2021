import customtkinter


import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class Login:
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    janela = customtkinter.CTk()
    janela.geometry("1000x800")

    texto = customtkinter.CTkLabel(janela, text="Login")

    email = customtkinter.CTkEntry(janela, placeholder_text="email")

    senha = customtkinter.CTkEntry(janela, placeholder_text="senha", show = "*")

    botao = customtkinter.CTkButton(janela, text=("Entrar"), command="clique")

    texto.pack(padx=20, pady=20)
    email.pack(padx=10, pady=10)
    senha.pack(padx=10, pady=10)
    botao.pack(padx=10, pady=10)

    janela.mainloop()