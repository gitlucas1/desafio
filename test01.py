from math import floor, ceil
from tkinter import *

def bt_click():
    Pontuacao = 50
    numNF = float(cx.get())
    numPF = float(cx1.get())


    if numNF > 0:
        cNF = 0
        while (cNF < numNF):
            cNF = cNF + 1
            Pontuacao = Pontuacao * 1.02
            Pontuacao = floor(Pontuacao)
    else:
        Pontuacao = Pontuacao

    if numPF > 0:
        cPF = 0
        while (cPF < numPF):
            cPF = cPF + 1
            Pontuacao = Pontuacao * 0.96
            Pontuacao = ceil(Pontuacao)
    else:
        Pontuacao = Pontuacao

    if Pontuacao < 0:
        Pontuacao = 1

    if Pontuacao > 100:
        Pontuacao = 100

    lb1["text"] = Pontuacao

janela = Tk()

lb = Label(janela, text="Nota Fiscal")
lb.place(x=120, y=20)
num = StringVar(value=0)
cx = Entry(janela, textvariable=num)
cx.place(x=90, y=40)


lb1 = Label(janela, text="")
lb1.place(x=140, y=200)

lb2 = Label(janela, text="Débitos")
lb2.place(x=125, y=70)
nume = StringVar(value=0)
cx1 = Entry(janela, textvariable=nume)
cx1.place(x=90, y=90)

bt = Button(janela, width=20, text="Calcular", command=bt_click)
bt.place(x=75, y= 250)
bt["bg"] = "violet"

janela.title("Desafio")

janela.geometry("300x300+200+200")

janela.mainloop()
