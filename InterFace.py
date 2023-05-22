# Peíodo de aprendizagem---

from tkinter import *
import functionsAcc

janela = Tk()
janela.title("ACCOUNTINGTEST101")
janela.configure(bg="black")

texto_orientacao = Label(janela, text="Clique no botão abaixo, para decidir sua ação")
texto_orientacao.grid(column=0, row=0)

texto_orientacao2 = Label(janela, text="Adicionar Saldo")
texto_orientacao2.grid(column=0, row=1)
botao = Button(janela, text="             ", command=functionsAcc.deposit)
codigo = Entry(janela, width=100)
botao.grid(column=0, row=2)


texto_orientacao3 = Label(janela, text="ver Tabela")
texto_orientacao3.grid(column=0, row=3)

botao2 = Button()
janela.mainloop()
