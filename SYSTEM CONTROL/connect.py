import mysql.connector
from PyQt5 import  uic,QtWidgets


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database='jacarandas'
  )

mycursor = mydb.cursor()



quant = 'SELECT qtd FROM Estoque WHERE codigo = 00000104'
mycursor.execute(quant)
myresult = mycursor.fetchall()
print(myresult[0][0]) #Devolve o INT da tabela







def busca(x:str):

  mycursor.execute("SELECT * FROM Estoque WHERE produto LIKE %s LIMIT 1", ("%" + x + "%",))

  print(myresult) 

  return myresult



def adcProduto(quantidade,codigo):
  
  sql = "UPDATE Estoque SET qtd = qtd + %s WHERE codigo = %s"
  val = (quantidade, codigo)

  mycursor.execute(sql, val)
  mydb.commit()






def venderProduto(quantidade,codigo):
  
  sql = "UPDATE Estoque SET qtd = qtd - %s WHERE codigo = %s"
  val = (quantidade, codigo)

  mycursor.execute(sql, val)
  mydb.commit()



#venderProduto("106", "00000104")
def menu_principal():
  menu.show()






def removerEstoque():
    remov.show()
    global linha1r
    global linha2r

    linha1r = remov.codigor.text()
    linha2r = remov.quantidader.text()
    venderProduto(linha2r,linha1r)

    

    print("Código:",linha1r)
    print("Descricao:",linha2r)
    remov.codigor.setText("")
    remov.quantidader.setText("")


def adcEstoque():
    formulario.show()
    global linha1
    global linha2

    linha1 = formulario.codigo.text()
    linha2 = formulario.quantidade.text()
    adcProduto(linha2,linha1)
    

    

    print("Código:",linha1)
    print("Descricao:",linha2)
    formulario.codigo.setText("")
    formulario.quantidade.setText("")

def listaprodutos():
  listprod.show()
  sql = 'SELECT * FROM Estoque'
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  print(myresult)
  listprod.tableWidget.setRowCount(len(myresult))
  listprod.tableWidget.setColumnCount(5)

  for x in range(0, len(myresult)):
    for y in range(0,5):
      listprod.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(myresult[x][y])))
      



    
    

app=QtWidgets.QApplication([])
#menu principal
menu=uic.loadUi("menu_Principal.ui")
menu.button_estoque.clicked.connect(adcEstoque)
menu.button_venda.clicked.connect(removerEstoque)

menu.show()
#-----tela de adc estoque
formulario=uic.loadUi("Estoque.ui")
formulario.button.clicked.connect(adcEstoque)
#-----tela de remover estoque
remov=uic.loadUi("Estoquer.ui")
remov.buttonr.clicked.connect(removerEstoque)
#-----tela de produtos
listprod=uic.loadUi("list.ui")
menu.button_produtos.clicked.connect(listaprodutos)

app.exec()
menu_principal()




