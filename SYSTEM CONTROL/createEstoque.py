import sqlite3

connection = sqlite3.connect("Estoque.db")

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS Estoque (codigo INTEGER PRIMARY KEY AUTOINCREMENT, produto varchar(30), valor decimal (5,2) not null, qtd int not null)"

cursor.execute(create_table)

tables = cursor.fetchall()