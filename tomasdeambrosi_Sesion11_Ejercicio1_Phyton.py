'''En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, 
la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.'''

import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

# Creamos la tabla
cur.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

# Insertamos información en la tabla
cur.execute("INSERT INTO Alumnos VALUES(1, 'Jorge', 'Rodríguez')")
cur.execute("INSERT INTO Alumnos VALUES(2, 'María', 'Alonso')")
cur.execute("INSERT INTO Alumnos VALUES(3, 'Julián', 'Díaz')")
cur.execute("INSERT INTO Alumnos VALUES(4, 'Julián', 'Pérez')")
cur.execute("INSERT INTO Alumnos VALUES(5, 'Natalia', 'Ochoa')")
cur.execute("INSERT INTO Alumnos VALUES(6, 'Mario', 'Bunge')")
cur.execute("INSERT INTO Alumnos VALUES(7, 'Héctor', 'Rawson')")
cur.execute("INSERT INTO Alumnos VALUES(8, 'Antonella', 'Altamira')")


# Guardamos los datos
con.commit()

# Seleccionamos los datos a buscar
cur.execute("SELECT * FROM Alumnos WHERE Nombre = 'Julián'")

resultado = cur.fetchall()

print(resultado)


# Cerramos el cursor y la conexión
cur.close
con.close()