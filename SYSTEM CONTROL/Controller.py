from PyQt5 import uic, QtWidgets
import sqlite3

def funcao_pincipal():

    linha1 = cadastro.lineEdit.text()
    linha2 = cadastro.lineEdit_2.text()
    linha3 = cadastro.lineEdit_3.text()

    if cadastro.radioButton_2.isChecked():
        print("Sexo Masculino foi selecionado")
        sexo = "Masculino"
    elif cadastro.radioButton.isChecked():
        print("Sexo Feminino foi selecionado")
        sexo = "Feminino"
    elif cadastro.radioButton_3.isChecked():
        print("Sexo Outro foi selecionado")
        sexo = "Outro"

    print("Nome:",linha1)
    print("Email:",linha2)
    print("Telefone:",linha3)

    connection = sqlite3.connect("cliente.db")

    cursor = connection.cursor()
    sql = "INSERT INTO Clientes(nome_completo,email,telefone,sexo) VALUES(?,?,?,?)"
    cursor.execute(sql,[linha1,linha2,linha3,sexo])
    connection.commit()

    connection.close()

    cadastro.lineEdit.setText("")
    cadastro.lineEdit_2.setText("")
    cadastro.lineEdit_3.setText("")

def chama_lista():
    lista.show()

    connection = sqlite3.connect("cliente.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM Clientes"
    cursor.execute(sql)
    tabela = cursor.fetchall()
    print(tabela)
    lista.tableWidget.setRowCount(len(tabela))
    lista.tableWidget.setColumnCount(5)

    for i in range(0,len(tabela)):
        for x in range(0,5):
            lista.tableWidget.setItem(i,x,QtWidgets.QTableWidgetItem(str(tabela[i][x])))

    connection.close()





""" exemplo sqlite conexao

    connection = sqlite3.connect("rpg.db")

    cursor = connection.cursor()

    sql = "SELECT * FROM Heroi WHERE id = (?)"
    cursor.execute(sql, [id_heroi])

    heroi = cursor.fetchone()

    if heroi == None:
        raise HeroiNaoExisteException
    
    connection.close()

"""



app=QtWidgets.QApplication([])
cadastro=uic.loadUi("PrototipoCadastroCliente.ui")
lista=uic.loadUi("PrototipoListaClientes.ui")
cadastro.pushButton.clicked.connect(funcao_pincipal)
cadastro.pushButton_2.clicked.connect(chama_lista)

cadastro.show()
app.exec()