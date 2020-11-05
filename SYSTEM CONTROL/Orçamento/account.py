from PyQt5 import uic, QtWidgets
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab import *
from datetime import date
from PyQt5.QtWidgets import *
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.lib.units import cm, mm, inch, pica
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def insertTable():
    connection = sqlite3.connect("accounts.db")
    linha1 = createa.nome.text()
    linha2 = createa.usuario.text()
    linha3 = createa.senha.text()
    linha4 = createa.senhac.text()
    sql = "SELECT * FROM user WHERE usuario = ?"
    cursor = connection.cursor()
    cursor.execute(sql,[linha2])
    results = cursor.fetchall()
    print(results)

    if linha1 == '' or linha2 == '' or linha3 == '' or linha4 == '':
        createa.label.setText("Preencha todos os campos")
    elif linha3 != linha4:
        createa.label.setText("Senhas não conferem")
    elif results == '':
        createa.label.setText("Usuario ja existe")
    else:
        cursor = connection.cursor()
        sql = "INSERT INTO user(cargo,nome,usuario,senha) VALUES(?,?,?,?)"
        cursor.execute(sql,['common',linha1,linha2,linha3])
        connection.commit()

        connection.close()

        linha1 = createa.nome.setText("")
        linha2 = createa.usuario.setText("")
        linha3 = createa.senha.setText("")
        linha4 = createa.senhac.setText("")


    
def check():
    connection = sqlite3.connect("accounts.db")
    usuario = login.usuario.text()
    senha = login.senha.text()

    cursor = connection.cursor()
    sql = ("SELECT * FROM user WHERE usuario = ? AND senha = ?")
    cursor.execute(sql,[usuario,senha])
    results = cursor.fetchall()
    sql2 = 'SELECT senha FROM user WHERE usuario = ?'
    cursor.execute(sql2,[usuario])
    results2 = cursor.fetchall()
    sql3 = 'SELECT usuario FROM user WHERE usuario = ?'
    cursor.execute(sql3,[usuario])
    results3 = cursor.fetchall()
    print(results2)

    if usuario == '' or senha == '':
        login.dados.setText("Preencha todos os campos")
    else:
        if results:
            menu.show()
            a = login.usuario.text()
            bemVindo = "Bem vindo " + a
            menu.bemVindo.setText(bemVindo)
            login.hide()
        elif results3 != []:
            if senha != results2[0]:
                login.dados.setText("Senha Incorreta")
        elif results3 == []:
            login.dados.setText("Usuario não existe")

def editStock():
    connection = sqlite3.connect("Estoque.db")
    cursor = connection.cursor()
    edit.show()
    menu.hide()
    edit.editmat.clear()
    edit.removemat.clear()
    sql = "SELECT Produto FROM Estoque"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    mat = [item for t in myresult for item in t]

    for i in range(0,len(mat)):
        print(mat[i])
        if edit.editmat.findData(i) != mat[i]:
            edit.editmat.insertItem(i,mat[i])
            edit.removemat.insertItem(i,mat[i])


    connection.close()
    edit.valor.setText("")
    edit.quantidade.setText("")

def adicionaMat():
    connection = sqlite3.connect("Estoque.db")
    cursor = connection.cursor()

    produto = edit.editmat.currentText()

    valor = edit.valor.text()
    qtd = edit.quantidade.text()
    sql = "UPDATE Estoque SET valor = ? , qtd = ? WHERE produto = ?"
    if valor != "" or qtd != "" :
        cursor.execute(sql,[valor,qtd,produto])
        connection.commit()
        connection.close()
    
def removeMat():
    connection = sqlite3.connect("Estoque.db")
    cursor = connection.cursor()

    produto = edit.removemat.currentText()

    sql = "DELETE FROM Estoque WHERE produto = ?;"
    cursor.execute(sql,[produto])
    connection.commit()
    editStock()
    connection.close()


'''def addStock():
    connection = sqlite3.connect("Estoque.db")
    cursor = connection.cursor()
    formulario.show()
    menu.hide()
    global linha1
    global linha2

    linha1 = formulario.codigo.text()
    linha2 = formulario.quantidade.text()
    sql = "UPDATE Estoque SET qtd = qtd + ? WHERE codigo = ?"

    cursor.execute(sql,[linha2,linha1])
    connection.commit()
    

    print("Código:",linha1)
    print("Descricao:",linha2)
    formulario.codigo.setText("")
    formulario.quantidade.setText("")'''

'''def removeStock():
    
    connection = sqlite3.connect("Estoque.db")
    cursor = connection.cursor()
    menu.hide()
    remov.show()
    global linha1r
    global linha2r

    linha1r = remov.codigor.text()
    linha2r = remov.quantidader.text()
    sql = "UPDATE Estoque SET qtd = qtd - ? WHERE codigo = ?"
    cursor.execute(sql,[linha2r,linha1r])
    connection.commit()

    print("Código:",linha1r)
    print("Descricao:",linha2r)
    remov.codigor.setText("")
    remov.quantidader.setText("")'''
def showmat():
    adcmat.show()
    menu.hide
def insert_service():
    connection = sqlite3.connect("Estoque.db")
    cursor = connection.cursor()
    global b
    global c
    global d
        
    
    b = adcmat.produto.text()
    c = adcmat.valor.text()
    d = adcmat.quantidade.text()


    sql = 'INSERT INTO Estoque ( produto,valor,qtd) VALUES (?,?,?)'
    cursor.execute(sql,[b,c,d])
    connection.commit()
    adcmat.produto.setText("")
    adcmat.valor.setText("")
    adcmat.quantidade.setText("")

def listProducts():
    connection = sqlite3.connect("Estoque.db")
    cursor = connection.cursor()
    menu.hide()
    listprod.show()
    sql = 'SELECT * FROM Estoque'
    cursor.execute(sql)
    myresult = cursor.fetchall()
    print(myresult)
    listprod.tableWidget.setRowCount(len(myresult))
    listprod.tableWidget.setColumnCount(4)
    lista = ['Codigo', 'Nome do Produto','Valor', 'Quantidade']
    listprod.tableWidget.setHorizontalHeaderLabels(list(lista))
    listprod.tableWidget.setColumnWidth(1,260)

    for x in range(0, len(myresult)):
        for y in range(0,4):
            listprod.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(myresult[x][y])))

def items_clear():
    for y in range(0,5):
        for x in range(0,4):
            listprod.tableWidget.setItem(y,x,QtWidgets.QTableWidgetItem(''))
      

def search():
    connection = sqlite3.connect("Estoque.db")
    cursor = connection.cursor()
    pesq = listprod.pesquisa.text() 
    sql ="SELECT * FROM Estoque WHERE codigo LIKE ?"
    pesq = '%' + pesq + '%'
    cursor.execute(sql,[pesq])
    myresult = cursor.fetchall()
    items_clear()
    listprod.tableWidget.setRowCount(len(myresult))
    listprod.tableWidget.setColumnCount(4)  
    for x in range(0, len(myresult)):
        for y in range(0,4):
            listprod.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(myresult[x][y])))
    print(myresult) 

def logout():
    menu.close()
    createa.close()
    login.show()
    login.usuario.setText("")
    login.senha.setText("")

def back():
    adcmat.hide()
    listprod.hide()
    edit.hide()
    orca.hide()
    menu.show()
    


def gerar_pdf():
    nome = orca.nome.text()
    cpf = orca.cpf.text()
    endereco = orca.endereco.text()
    bairro = orca.bairro.text()
    cidade = orca.cidade.text()
    cep = orca.cep.text()
    telefone = orca.telefone.text()
    email = orca.email.text()
    email2 = orca.email_2.text()
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
    existing_pdf = PdfFileReader(open("system_control_mecanica_666.pdf", "rb"))
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
    email2 = orca.email_2.text()
    modelo = orca.modelo.text()
    marca = orca.marca.text()
    ano = orca.ano.text()
    placa = orca.placa.text()
    km = orca.km.text()
    data = orca.data.text()

    if email != email2:
        orca.label_21.setText("Emails não conferem")
    elif nome and cpf and endereco and telefone and cidade and bairro and cep and modelo and marca and ano and placa and km and email and email2 and data != "":
        gerar_pdf()
        orca.label_21.setText("PDF gerado")
        orca.label_21.setStyleSheet("background-color: lightgreen")
    else:
        orca.label_21.setText("Confira seus Dados")

    







#-----tela de criação do usuario
app=QtWidgets.QApplication([])
createa=uic.loadUi("usuario.ui")
createa.button.clicked.connect(insertTable)
createa.voltar.clicked.connect(logout)


#tela de login
login=uic.loadUi("user.ui")
login.semconta.clicked.connect(createa.show)
login.logar.clicked.connect(check)
login.show()
#-----tela de material
adcmat=uic.loadUi("adcmaterial.ui")
adcmat.button.clicked.connect(insert_service)
adcmat.voltar.clicked.connect(back)

#-----tela de produtos
listprod=uic.loadUi("list.ui")
listprod.buttonp.clicked.connect(search)
listprod.voltar.clicked.connect(back)

'''#-----tela de remover estoque
remov=uic.loadUi("Estoquer.ui")
remov.buttonr.clicked.connect(removeStock)
remov.voltar.clicked.connect(back)'''

'''#-----tela de adc estoque
formulario=uic.loadUi("Estoque.ui")
formulario.button.clicked.connect(addStock)
formulario.voltar.clicked.connect(back)'''

#-----tela de editar material
edit=uic.loadUi("editarmaterial.ui")
edit.button.clicked.connect(adicionaMat)
edit.button_2.clicked.connect(removeMat)
edit.voltar.clicked.connect(back)

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
email2 = orca.email_2.text()
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
orca.voltar.clicked.connect(back)
#menu princpal
menu=uic.loadUi("menu_Principal.ui")
menu.button_estoque_2.clicked.connect(editStock)
menu.material.clicked.connect(showmat)
menu.button_produtos.clicked.connect(listProducts)
menu.logout.clicked.connect(logout)
menu.button_orca.clicked.connect(orca.show)







app.exec()

        




