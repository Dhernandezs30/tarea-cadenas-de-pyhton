correo = input("Introduce tu correo electrónico: ")

nombre_usuario = correo.split("@")[0]  # Se obtiene la parte del nombre del correo
nuevo_correo = nombre_usuario + "@ceu.es"

print(nuevo_correo)
