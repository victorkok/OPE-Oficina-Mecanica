import mysql.connector
from PyQt5 import  uic,QtWidgets


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database='jacarandas'
  )

mycursor = mydb.cursor()



'''quant = 'SELECT qtd FROM Estoque WHERE codigo = 1'
mycursor.execute(quant)
myresult = mycursor.fetchall()
print(myresult)'''

usu = 'SELECT * FROM user where usuario = root'

mycursor.execute(usu)
myresult = mycursor.fetchall()
print(myresult)


def items_clear():
  listprod.tableWidget.setRowCount(len(myresult))
  listprod.tableWidget.setColumnCount(4)  
  for y in range(0, len(myresult)):
    for x in range(0,4):
      listprod.tableWidget.setItem(y,x,QtWidgets.QTableWidgetItem(''))





def search(x:str):
  pesq = listprod.pesquisa.text()
  busca(pesq) 
  mycursor.execute("SELECT * FROM Estoque WHERE produto LIKE %s", ("%" + x + "%",))
  myresult = mycursor.fetchall()
  items_clear()
  listprod.tableWidget.setRowCount(len(myresult))
  listprod.tableWidget.setColumnCount(4)
  for x in range(0, len(myresult)):
    for y in range(0,4):
      listprod.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(myresult[x][y])))
  print(myresult) 








#venderProduto("106", "00000104")
def menu_principal():
  menu.show()



def insert_service():
  global b
  global c
  global d
    
  
  b = adcmat.produto.text()
  c = adcmat.valor.text()
  d = adcmat.quantidade.text()


  sql = 'INSERT INTO Estoque ( produto,valor,qtd) VALUES (%s,%s,%s)'
  values = (b, c, d)
  mycursor.execute(sql,values)
  mydb.commit()
  adcmat.produto.setText("")
  adcmat.valor.setText("")
  adcmat.quantidade.setText("")



  




def removerEstoque():
  remov.show()
  global linha1r
  global linha2r

  linha1r = remov.codigor.text()
  linha2r = remov.quantidader.text()
  sql = "UPDATE Estoque SET qtd = qtd - %s WHERE codigo = %s"
  val = (quantidade, codigo)

  mycursor.execute(sql, val)
  mydb.commit()

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
  sql = "UPDATE Estoque SET qtd = qtd + %s WHERE codigo = %s"
  val = (quantidade, codigo)

  mycursor.execute(sql, val)
  mydb.commit()

  print("Código:",linha1)
  print("Descricao:",linha2)
  formulario.codigo.setText("")
  formulario.quantidade.setText("")

def listProducts():
  listprod.show()
  sql = 'SELECT * FROM Estoque'
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  print(myresult)
  listprod.tableWidget.setRowCount(len(myresult))
  listprod.tableWidget.setColumnCount(4)
  lista = ['Codigo', 'Nome do Produto','Valor', 'Quantidade']
  listprod.tableWidget.setHorizontalHeaderLabels(list(lista))
  listprod.tableWidget.setColumnWidth(1,260)

  for x in range(0, len(myresult)):
    for y in range(0,4):
      listprod.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(myresult[x][y])))
      

def entrarconta():
  linha1 = login.usuario.setText()
  linha2 = login.senha.setText()
  
  usu = f'SELECT qtd FROM Estoque WHERE user = admin'

  mycursor.execute(usu)
  myresult = mycursor.fetchall()
  print(myresult)




    
    

app=QtWidgets.QApplication([])
#menu principal
menu=uic.loadUi("menu_Principal.ui")
menu.button_estoque.clicked.connect(adcEstoque)
menu.button_venda.clicked.connect(removerEstoque)
menu.material.clicked.connect(adcmat.show)

menu.show()
#-----tela de adc estoque
formulario=uic.loadUi("Estoque.ui")
formulario.button.clicked.connect(adcEstoque)
#-----tela de remover estoque
remov=uic.loadUi("Estoquer.ui")
remov.buttonr.clicked.connect(removerEstoque)
#-----tela de produtos
listprod=uic.loadUi("list.ui")
menu.button_produtos.clicked.connect(listProducts)
listprod.buttonp.clicked.connect(search)
#-----tela de material
adcmat=uic.loadUi("adcmaterial.ui")
adcmat.button.clicked.connect(insert_service)
#-----tela de login
#-----tela de material
login=uic.loadUi("user.ui")
login.button.clicked.connect()

app.exec()
menu_principal()




