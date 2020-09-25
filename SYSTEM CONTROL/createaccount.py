import sqlite3

connection = sqlite3.connect("accounts.db")

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS user (cargo varchar(30), nome varchar(20), usuario varchar(30), senha varchar(30))"

cursor.execute(create_table)

tables = cursor.fetchall()