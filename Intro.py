
from tkinter import *
from PIL import ImageTk, Image


class splash:
    def __init__(self):
        self.splashmainw = Tk()
        self.splashmainw.title("CURSO DE VENDAS EM PYTHON TKINTER :")
        width = 1000
        height = 680

        self.splashmainw.iconbitmap(r'C:\Sistema_vendas_tkinter_copia\images\icon.ico')

        self.splashmainw.config(bg="darkorange")
        tela_largura = self.splashmainw.winfo_screenwidth()
        tela_altura = self.splashmainw.winfo_screenheight()
        x = (tela_largura / 2 ) - (width /2 )
        y = (tela_altura / 2 ) - (height /2 )
        self.splashmainw.geometry("%dx%d+%d+%d" % (width,height,x,y))
        self.splashmainw.resizable(0,0)
        path ="images/intro.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        main = LabelFrame(self.splashmainw,width=890,height=560,bg="lightsalmon",relief="sunken",bd="0")
        main.place(x=55,y=70)
        fotoframe = LabelFrame(main,width=420,height=444,bg="lightsalmon",relief="raised",bd="0")
        foto=Label(fotoframe,image=img)
        foto.place(x=6,y=6)
        fotoframe.place(x=10,y=100)

        Label(main, text="SISTEMA DE VENDAS EM TKINTER SQLITE",font="roboto 28 bold underline",bg="lightsalmon").place(x=45, y=10)
        Label(main, text="Sangiorgiovba",font="roboto 32 bold",bg="lightsalmon").place(x=450, y=160)
        Label(main, text="Programador",font="roboto 16 bold",bg="lightsalmon").place(x=445+5, y=260)
        Label(main, text="Desenvolvedor", font="roboto 16 bold", bg="lightsalmon").place(x=450, y=310)
        Label(main, text="Email : sangiorgiovba@gmail.com",font="roboto 16 bold",bg="lightsalmon").place(x=445+5, y=360)
        Label(main, text="Telefone : (------------------------)",font="roboto 16 bold",bg="lightsalmon").place(x=445+5, y=410)
       
       

        self.splashmainw.mainloop()
