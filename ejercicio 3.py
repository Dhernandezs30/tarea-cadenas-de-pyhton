nombre = input("Introduce tu nombre: ")
nombre_mayusculas = nombre.upper()
longitud = len(nombre.replace(" ", ""))  # Se eliminan los espacios para contar solo las letras

print(f"{nombre_mayusculas} tiene {longitud} letras")
