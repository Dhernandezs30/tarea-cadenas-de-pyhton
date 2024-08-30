frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

frase_modificada = frase.replace(vocal, vocal.upper())  # Reemplaza la vocal por su versión mayúscula

print(frase_modificada)
