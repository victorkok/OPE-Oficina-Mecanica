from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import date
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *


def gerar_pdf():
    nome = orca.nome.text()
    cpf = orca.cpf.text()
    rg = orca.rg.text()
    telefone = orca.telefone.text()
    endereco = orca.endereco.text()
    cidade = orca.cidade.text()
    bairro = orca.bairro.text()
    modelo = orca.modelo.text()
    marca = orca.marca.text()
    ano = orca.ano.text()
    placa = orca.placa.text()
    valor = orca.valor.text()

    global canvas
    canvas = canvas.Canvas(nome +".pdf", pagesize=letter)

    data_atual = date.today()

    data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
    data_atual.year)
    data_em_texto = str(data_em_texto)


    
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 20)

    canvas.drawString(230,750,'OFICINA JACARANDAS')
    canvas.setFont('Helvetica-Bold', 12)

    canvas.drawString(250,720,'ORÇAMENTO')
    canvas.setFont('Helvetica', 12)

    #Informações do Cliente
    canvas.drawString(30,650,"Nome: " + nome.title())
    canvas.drawString(300,650,'CPF: ' + cpf)
    canvas.drawString(510,722,data_em_texto)
    canvas.line(500,720,580,720)
    canvas.drawString(30,610,"RG: " + rg)
    canvas.drawString(300,610,"Telefone: " + telefone)
    canvas.drawString(30,570,'Endereço: ' + endereco.title())
    canvas.drawString(300,570,"Cidade: " + cidade.title())
    canvas.drawString(30,530,'Bairro: ' + bairro)

    #Informações do Veiculo
    canvas.setFont('Helvetica-Bold', 12)
    canvas.drawString(30,480,'Informações do Veiculo')
    canvas.setFont('Helvetica', 12)
    canvas.drawString(30,450, "Marca:" + marca)
    canvas.drawString(200,450, "Modelo:" + modelo.upper())
    canvas.drawString(390,450, "Ano:" + ano)
    canvas.drawString(30,420, "Cor: ")
    canvas.drawString(200,420, "Placa: " + placa.upper())

    #Informações do Serviço
    canvas.setFont('Helvetica-Bold', 12)
    canvas.drawString(30,370,'Informações do Serviço')
    canvas.setFont('Helvetica', 12)
    canvas.drawString(30,340,'Descrição do Problema')
    canvas.drawString(30,330,'')
    canvas.drawString(30,200,'Realizar: ' )
    






    canvas.setFont('Helvetica-Bold', 12)
    canvas.drawString(30,480,'Informações do Veiculo')




    canvas.save()



app=QtWidgets.QApplication([])
orca=uic.loadUi("orcamento.ui")


lista = ["Prata","Preto","Cinza","Branco","Vermelho","Azul","Verde","Amarelo"]
lista.sort()
orca.cor.setEditable(True)
cor = orca.cor.addItems(lista)

nome = orca.nome.text()
cpf = orca.cpf.text()
rg = orca.rg.text()
telefone = orca.telefone.text()
endereco = orca.endereco.text()
cidade = orca.cidade.text()
bairro = orca.bairro.text()
modelo = orca.modelo.text()
marca = orca.marca.text()
ano = orca.ano.text()
placa = orca.placa.text()
valor = orca.valor.text()
orca.confirm.clicked.connect(gerar_pdf)
orca.show()

app.exec()
