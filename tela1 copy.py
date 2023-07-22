
from tkinter import *
import requests
import sqlite3

#TELA PRINCIPAL




root = Tk()
root.geometry('600x500')
root.minsize(600, 500)
root.maxsize(600, 500)
root.title("UZC.co - Gerenciador de Pedidos")

#===============TITULO E IMAGEM========================================================
title = Label(text="UZC Company", font="Arial 20")
logo = PhotoImage(file="logo/uzclogo3.png").subsample(7,7)
label_logo = Label(image=logo)

#===================FUNCOES========================================================

#==============ACHAR O VALOR DO DOLAR==================
def procura_dolar():
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    dolar = requisicao.json()
    
    cotacao_dolar = dolar['USDBRL']['bid']


    usd = (f'Dolar: {cotacao_dolar} USD')

    valor_dolar["text"] = usd

#==========CADASTRAR PEDIDO===========================
def cadastrar_pedido():

    tela_cadastro = Tk()

    tela_cadastro.geometry('500x300')
    tela_cadastro.minsize(500,300)
    tela_cadastro.maxsize(500, 300)
    tela_cadastro.title("Cadastrando camisa")

    #Titulo da tela de cadastro
    titulo_cadastro = Label(tela_cadastro, text="CADASTRAR", font = "arial 15")

    camisa_text = Label(tela_cadastro, text="Camisa: ")
    camisa_input = Entry(tela_cadastro)

    cliente_text = Label(tela_cadastro, text = "Cliente: ")
    cliente_input = Entry(tela_cadastro)






    
#=====================LAYOUT PAGINA CADASTRO===============================================
    titulo_cadastro.grid(column=2, row=1)


    camisa_text.grid(column=1,row=2)
    camisa_input.grid(column=2, row=2)

    
    tela_cadastro.mainloop()
     


#================VARIAVEIS PAG INICIAL=================================================================
dolar = Button(root, text="Verificar Dólar/USD", font="Arial 10", command= procura_dolar)

cadastrar = Button(root, text="Cadastrar Pedido",font="Arial 15", command = cadastrar_pedido)

pedidos = Button(root, text="Ver pedidos", font="Arial 15")

valor_dolar = Label(root, text="")




#====================LAYOUT PAGINA INICIAL================================================
title.grid(column=2, row=1, pady=(50,0))
label_logo.grid(column=2, row=2)
cadastrar.grid(column=1, row=3, padx=(50,0))
pedidos.grid(column=3, row=3, padx=(0,50))
dolar.grid(column=2, row=4, pady=(75,0))
valor_dolar.grid(column=2, row=5)

root.mainloop()