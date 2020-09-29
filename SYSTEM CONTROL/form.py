from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab import *
from datetime import date
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *


def verificador ():
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
    cor = orca.cor.currentText()
    desc = orca.descricao.toPlainText()

    if nome and cpf and rg and telefone and endereco and cidade and bairro and modelo and marca and ano and placa and valor != "":
        gerar_pdf()
        orca.label_21.setText("PDF gerado")
        orca.label_21.setStyleSheet("background-color: lightgreen")
    else:
        orca.label_21.setText("Confira seus Dados")
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
    cor = orca.cor.currentText()
    desc = orca.descricao.toPlainText()
    data = orca.data.text()


    

    funilaria = orca.funilaria.isChecked()
    pintura = orca.pintura.isChecked()



    global canvas
    canvas = canvas.Canvas(nome +".pdf", pagesize=letter)

    data_atual = date.today()

    data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
    data_atual.year)
    data_em_texto = str(data_em_texto)


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
    canvas.drawString(30,420, "Cor: " + cor)
    canvas.drawString(200,420, "Placa: " + placa.upper())

    #Informações do Serviço
    canvas.setFont('Helvetica-Bold', 12)
    canvas.drawString(30,370,'Informações do Serviço')
    canvas.setFont('Helvetica', 12)
    canvas.drawString(30,340,'Descrição do Problema')
    y = 0
    z = 103
    h = 320
    for x in range(6):
        canvas.drawString(30,h,desc[y:z])
        y = z + 1
        z = z + 103
        h = h-20

    
    if funilaria == True and pintura == True:
        canvas.drawString(30,200,'Realizar : Funilaria e Pintura')
    if funilaria == True and pintura == False:
        canvas.drawString(30,200,'Realizar : Funilaria')
    if funilaria == False and pintura == True:
        canvas.drawString(30,200,'Realizar : Pintura')

    canvas.drawString(30,110, 'Data da Retirada:')
    canvas.drawString(30,90, data)
    canvas.drawString(500,110, 'VALOR:')
    canvas.drawString(500,90, valor)



    canvas.setFont('Helvetica-Bold', 12)
    canvas.drawString(30,480,'Informações do Veiculo')


    print(desc)



    canvas.save()



app=QtWidgets.QApplication([])
orca=uic.loadUi("orcamento.ui")


lista = ["Prata","Preto","Cinza","Branco","Vermelho","Azul","Verde","Amarelo"]
lista.sort()
orca.cor.setEditable(True)
orca.descricao.setWordWrapMode(3)
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
orca.confirm.clicked.connect(verificador)
orca.cancel.clicked.connect(orca.close)
orca.telefone.setInputMask('(00)00000-0000')
orca.placa.setInputMask('AAA-0000')
orca.cpf.setInputMask("000-000-000/00")
orca.rg.setInputMask("00.000.000-0")
orca.data.installEventFilter(orca.data.setInputMask('99/99/9999'))
orca.data.setPlaceholderText('MM/DD/YYYY')
orca.valor.setInputMask("009.99;_")


orca.show()

app.exec()
