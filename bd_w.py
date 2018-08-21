import sqlite3

conn = sqlite3.connect('aula.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Alunos(Nome TEXT, Matrícula REAL, Idade INTEGER, Ingresso INTEGER, Situação TEXT )")

def data_entry():
    c.execute("INSERT INTO Alunos VALUES('Henrique',11202989,26,2011,'Cursando')")

create_table()
data_entry()

conn.commit()
c.close()
conn.close()
