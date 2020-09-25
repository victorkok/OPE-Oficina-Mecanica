import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database='jacarandas'
  )

mycursor = mydb.cursor()

muycursor.execute('SELECT *FROM user WHERE cargo = admin')
mycursor.fetchall()
printmycursor.fetchall()


