def obtener_numero_principal():
    telefono = input("Introduce el número de teléfono en formato +34-número-extensión: ")
    
    # Dividir el número de teléfono por el separador '-'
    partes = telefono.split('-')
    
    if len(partes) == 3 and partes[0] == '+34':
        numero_principal = partes[1]
        print("El número de teléfono sin prefijo y extensión es:", numero_principal)
    else:
        print("El formato del número de teléfono es incorrecto. Asegúrate de usar el formato +34-número-extensión.")

obtener_numero_principal()
