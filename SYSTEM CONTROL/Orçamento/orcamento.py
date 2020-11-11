from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab import *
from datetime import date
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm, mm, inch, pica
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import date

def gerar_pdf():
    nome = orca.nome.text()
    cpf = orca.cpf.text()
    endereco = orca.endereco.text()
    bairro = orca.bairro.text()
    cidade = orca.cidade.text()
    cep = orca.cep.text()
    telefone = orca.telefone.text()
    email = orca.email.text()
    modelo = orca.modelo.text()
    marca = orca.marca.text()
    ano = orca.ano.text()
    placa = orca.placa.text()
    km = orca.km.text()
    data = orca.data.text()
    cor = orca.cor.currentText()


    data_atual = date.today()

    data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
    data_atual.year)
    data_em_texto = str(data_em_texto)

    pdfmetrics.registerFont(TTFont('Times-New-Roman',
    'c:\\windows\\fonts\\times.ttf'))
    pdfmetrics.registerFont(TTFont('Times-New-RomanBd',
    'c:\\windows\\fonts\\timesBd.ttf'))
    pdfmetrics.registerFont(TTFont('Times-New-RomanIt',
    'c:\\windows\\fonts\\timesI.ttf'))
    pdfmetrics.registerFont(TTFont('Times-New-RomanBI',
    'c:\\windows\\fonts\\timesBI.ttf'))

    packet = io.BytesIO()
    # Veiculo
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont('Times-New-Roman', 12)
    #Modelo
    can.drawString(72, 701, modelo.upper())
    #Marca
    can.drawString(72, 687, marca.upper())
    #Cor
    can.drawString(55, 673, cor)
    #Ano
    can.drawString(202, 701, ano)
    #Placa
    can.drawString(208, 687, placa.upper())
    #Km
    can.drawString(200, 673, km +' Km')
    #Data da Retirada
    can.drawString(500, 701, data)



    #Cliente
    can.setFont('Times-New-Roman', 10)
    #Nome
    can.drawString(70, 191, nome.title())
    #CPF
    can.drawString(83, 181, cpf)
    #Endereço
    can.drawString(73, 168, endereco.title())
    #Bairro
    can.drawString(65, 157, bairro.title())
    #Telefone
    can.drawString(75, 146, telefone)
    #Email
    can.drawString(65, 134, email)
    #Cidade
    can.drawString(385, 191, cidade.title())
    #CEP
    can.drawString(375, 181, cep)









    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("pokas.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open(nome +".pdf", "wb")
    output.write(outputStream)
    outputStream.close()





def verificador ():
    nome = orca.nome.text()
    cpf = orca.cpf.text()
    endereco = orca.endereco.text()
    bairro = orca.bairro.text()
    cidade = orca.cidade.text()
    cep = orca.cep.text()
    telefone = orca.telefone.text()
    email = orca.email.text()
    modelo = orca.modelo.text()
    marca = orca.marca.text()
    ano = orca.ano.text()
    placa = orca.placa.text()
    km = orca.km.text()
    data = orca.data.text()

    
    if nome and cpf and endereco and telefone and cidade and bairro and cep and modelo and marca and ano and placa and km and email and data != "":
        gerar_pdf()
        orca.label_21.setText("PDF gerado")
        orca.label_21.setStyleSheet("background-color: lightgreen")
    else:
        orca.label_21.setText("Confira seus Dados")















app=QtWidgets.QApplication([])
orca=uic.loadUi("orcamento.ui")


lista = ["Prata","Preto","Cinza","Branco","Vermelho","Azul","Verde","Amarelo"]
lista.sort()
orca.cor.setEditable(True)
cor = orca.cor.addItems(lista)

nome = orca.nome.text()
cpf = orca.cpf.text()
endereco = orca.endereco.text()
bairro = orca.bairro.text()
cidade = orca.cidade.text()
cep = orca.cep.text()
telefone = orca.telefone.text()
email = orca.email.text()
modelo = orca.modelo.text()
marca = orca.marca.text()
ano = orca.ano.text()
placa = orca.placa.text()
km = orca.km.text()
orca.confirm.clicked.connect(verificador)
orca.cancel.clicked.connect(orca.close)
orca.telefone.setInputMask('(00)00000-0000')
orca.placa.setInputMask('AAA-0000')
orca.cpf.setInputMask("000-000-000/00")
orca.data.installEventFilter(orca.data.setInputMask('99/99/9999'))
orca.data.setPlaceholderText('MM/DD/YYYY')
orca.cep.setInputMask('00000-000')
orca.km.setInputMask('000000')
orca.ano.setInputMask('0000')




orca.show()

app.exec()
