#Pablo Dario Jimenez Nu*o 21310143

import sqlite3

# Conectarse a la base de datos (si no existe, se creará un nuevo archivo de base de datos)
conn = sqlite3.connect('example.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear una tabla (si no existe)
cursor.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insertar datos
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('Alice', 20))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('Bob', 22))

# Guardar los cambios
conn.commit()

# Recuperar datos
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# Mostrar los datos recuperados
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()


























