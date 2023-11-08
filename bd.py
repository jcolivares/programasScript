import sqlite3 as sql

#Establecer una conexion a la base de datos
conexion = sql.Connection("ejemplo.db")

#establecer un cursor
db = conexion.cursor()

#insercion
sql = """INSERT INTO usuarios 
    VALUES ( 2, 
    'jperez',
    'jperez',
    2
    )
"""

resultado = db.execute(sql)
conexion.commit()

conexion.close()

