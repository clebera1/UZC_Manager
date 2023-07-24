
from tkinter import *
import requests
import sqlite3
import os
#=====================CADASTRAR PEDIDO=====================================================
def cadastrar_pedido():
        camisa = camisa_input.get()
        cliente = cliente_input.get()
        tamanho = tamanho_input.get()


    #criar conexao com banco e criar tabela
        banco = sqlite3.connect('registros_camisas.db')
        cursor = banco.cursor()

    #efetivamente cadastrar os jogadores no banco 
        cursor.execute('''CREATE TABLE IF NOT EXISTS registros_camisas(camisa TEXT, cliente TEXT, tamanho TEXT)''')
        cursor.execute("INSERT INTO registros_camisas VALUES (?, ?, ?)", (camisa, cliente, tamanho))

    #comitar alterações e fechar conexao com banco 
        banco.commit()
        banco.close()

        #==========ABRIR TELA CADASTRO PEDIDO===========================
def abrir_tela_cadastro():
    
    global camisa_input, cliente_input, tamanho_input

    tela_cadastro = Toplevel()
    tela_cadastro.geometry('680x360')
    #tela_cadastro.minsize(700,200)
    #tela_cadastro.maxsize(700, 200)
    tela_cadastro.title("Cadastrando camisa")

    titulo_cadastro = Label(tela_cadastro, text="Tela de Cadastro", font = "arial 15")



    logo_cadastro = PhotoImage(file=pastaApp+"\\logo\\uzclogo3.png").subsample(7,7)
    label_logo_cadastro = Label(tela_cadastro, image=logo_cadastro)



    camisa_text = Label(tela_cadastro, text="Camisa: ")
    camisa_input = Entry(tela_cadastro)

    cliente_text = Label(tela_cadastro, text = "Cliente: ")
    cliente_input = Entry(tela_cadastro)

    tamanho_text = Label(tela_cadastro, text = "Tamanho: ")
    tamanho_input = Entry(tela_cadastro)

    cadastrar_camisa = Button (tela_cadastro, text='CADASTRAR CAMISA', font = 'Arial 10', command=  cadastrar_pedido)

    #=====================LAYOUT PAGINA CADASTRO===============================================
    titulo_cadastro.grid(column=4, row=1, pady = 20)
    label_logo_cadastro.grid(column=4, row = 2)



    camisa_text.grid(column=1,row=3, padx= 5)
    camisa_input.grid(column=2, row=3)

    cliente_text.grid(column=3, row=3, padx= 5)
    cliente_input.grid(column=4, row=3)

    tamanho_text.grid(column=5, row=3, padx= 5)
    tamanho_input.grid(column=6, row=3)

    cadastrar_camisa.grid(column=4, row =4, pady=25)


    tela_cadastro.mainloop()

#==================FUNCOES========================================================

#==============ACHAR O VALOR DO DOLAR==================
def procura_dolar():
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    dolar = requisicao.json()
    
    cotacao_dolar = dolar['USDBRL']['bid']


    usd = (f'Dolar: {cotacao_dolar} USD')

    valor_dolar["text"] = usd

    #TELA PRINCIPAL

pastaApp = os.path.dirname(__file__)

root = Tk()
root.geometry('550x450')
root.minsize(550, 450)
root.maxsize(550, 450)
root.title("UZC.co - Gerenciador de Pedidos")

#===============TITULO E IMAGEM========================================================
title = Label(text="UZC Company", font="Arial 20")
logo = PhotoImage(file="logo/uzclogo3.png").subsample(7,7)
label_logo = Label(root,image=logo)

    



#===============TITULO IMAGEM TELA INICIAL=====================================




     


#================VARIAVEIS PAG INICIAL=================================================================
dolar = Button(root, text="Verificar Dólar/USD", font="Arial 10", command= procura_dolar)

cadastrar = Button(root, text="CADASTRAR",font="Arial 15", command = abrir_tela_cadastro)

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