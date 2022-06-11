import sqlite3

nombreBD = "prueba.db"
conexion  = sqlite3.connect(nombreBD)
print(f'{nombreBD} opened')

conexion.execute('''CREATE TABLE personas
                 (id INT PRIMARY KEY NOT NULL,
                 nombre TEXT NOT NULL,
                 ))