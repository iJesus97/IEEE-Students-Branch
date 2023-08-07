import tkinter as tk
import sqlite3

# Crear la conexión a la base de datos
conn = sqlite3.connect('datos.db')
cursor = conn.cursor()

# Crear la tabla para los datos del carrusel
cursor.execute('''CREATE TABLE IF NOT EXISTS carrusel
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT,
                   contenido TEXT,
                   boton TEXT)''')

# Crear la tabla para los datos del post y las imágenes
cursor.execute('''CREATE TABLE IF NOT EXISTS datos
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   tipo TEXT,
                   titulo TEXT,
                   autor TEXT,
                   fecha TEXT,
                   contenido TEXT,
                   ruta_imagen TEXT,
                   pie_pagina TEXT)''')

# Función para guardar los datos del carrusel
def guardar_carrusel():
    titulo = entry_titulo_carrusel.get()
    contenido = entry_contenido_carrusel.get()
    boton = entry_boton_carrusel.get()
    
    # Insertar los datos en la base de datos
    cursor.execute("INSERT INTO carrusel (titulo, contenido, boton) VALUES (?, ?, ?)",
                   (titulo, contenido, boton))
    conn.commit()
    
    # Limpiar los campos de entrada
    entry_titulo_carrusel.delete(0, tk.END)
    entry_contenido_carrusel.delete(0, tk.END)
    entry_boton_carrusel.delete(0, tk.END)

# Función para guardar los datos del post y las imágenes
def guardar_datos():
    tipo = "post"
    titulo = entry_titulo_post.get()
    autor = entry_autor.get()
    fecha = entry_fecha.get()
    contenido = entry_contenido_post.get()
    
    # Insertar los datos del post en la base de datos
    cursor.execute("INSERT INTO datos (tipo, titulo, autor, fecha, contenido) VALUES (?, ?, ?, ?, ?)",
                   (tipo, titulo, autor, fecha, contenido))
    
    # Obtener los datos de las imágenes
    for campo_imagen, campo_pie in campos_imagenes:
        tipo = "imagen"
        ruta_imagen = campo_imagen.get()
        pie_pagina = campo_pie.get()
        
        # Insertar los datos de las imágenes en la base de datos
        cursor.execute("INSERT INTO datos (tipo, titulo, autor, fecha, contenido, ruta_imagen, pie_pagina) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (tipo, titulo, autor, fecha, contenido, ruta_imagen, pie_pagina))
    
    conn.commit()
    
    # Limpiar los campos de entrada
    entry_titulo_post.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)
    entry_contenido_post.delete(0, tk.END)
    
    for campo_imagen, campo_pie in campos_imagenes:
        campo_imagen.delete(0, tk.END)
        campo_pie.delete(0, tk.END)

# Función para agregar campos adicionales de imagen y pies de página
def agregar_campos_imagenes():
    num_campos = int(entry_num_campos.get())
    
    # Crear campos adicionales de imagen y pies de página
    for i in range(num_campos):
        label_ruta_imagen = tk.Label(window, text=f"Ruta de la imagen {i+1}:")
        label_ruta_imagen.pack()
        entry_ruta_imagen = tk.Entry(window)
        entry_ruta_imagen.pack()
        
        label_pie_pagina = tk.Label(window, text=f"Pie de página {i+1}:")
        label_pie_pagina.pack()
        entry_pie_pagina = tk.Entry(window)
        entry_pie_pagina.pack()
        
        campos_imagenes.append((entry_ruta_imagen, entry_pie_pagina))
    
    # Actualizar la interfaz
    btn_agregar_campos.config(state=tk.DISABLED)

# Crear la ventana principal
window = tk.Tk()

# Sección de datos del carrusel
label_titulo_carrusel = tk.Label(window, text="Título del carrusel:")
label_titulo_carrusel.pack()
entry_titulo_carrusel = tk.Entry(window)
entry_titulo_carrusel.pack()

label_contenido_carrusel = tk.Label(window, text="Contenido:")
label_contenido_carrusel.pack()
entry_contenido_carrusel = tk.Entry(window)
entry_contenido_carrusel.pack()

label_boton_carrusel = tk.Label(window, text="Botón:")
label_boton_carrusel.pack()
entry_boton_carrusel = tk.Entry(window)
entry_boton_carrusel.pack()

btn_guardar_carrusel = tk.Button(window, text="Guardar Carrusel", command=guardar_carrusel)
btn_guardar_carrusel.pack()

# Sección de datos del post
label_titulo_post = tk.Label(window, text="Título del post:")
label_titulo_post.pack()
entry_titulo_post = tk.Entry(window)
entry_titulo_post.pack()

label_autor = tk.Label(window, text="Autor:")
label_autor.pack()
entry_autor = tk.Entry(window)
entry_autor.pack()

label_fecha = tk.Label(window, text="Fecha:")
label_fecha.pack()
entry_fecha = tk.Entry(window)
entry_fecha.pack()

label_contenido_post = tk.Label(window, text="Contenido:")
label_contenido_post.pack()
entry_contenido_post = tk.Entry(window)
entry_contenido_post.pack()

btn_guardar_datos = tk.Button(window, text="Guardar Datos", command=guardar_datos)
btn_guardar_datos.pack()

# Sección para agregar campos adicionales de imagen y pies de página
label_num_campos = tk.Label(window, text="Número de campos de imagen:")
label_num_campos.pack()
entry_num_campos = tk.Entry(window)
entry_num_campos.pack()

btn_agregar_campos = tk.Button(window, text="Agregar Campos", command=agregar_campos_imagenes)
btn_agregar_campos.pack()

campos_imagenes = []  # Lista para almacenar los campos de imagen y pies de página adicionales

# Ejecutar la interfaz
window.mainloop()

# Cerrar la conexión a la base de datos al salir de la aplicación
conn.close()
