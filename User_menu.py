
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox




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

