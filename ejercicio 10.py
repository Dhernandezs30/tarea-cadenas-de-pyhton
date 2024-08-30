productos = input("Introduce los productos de la cesta de la compra, separados por comas: ")

lista_productos = productos.split(",")  # Se separan los productos por comas

for producto in lista_productos:
    print(producto.strip())  # Imprime cada producto en una línea diferente, eliminando espacios en blanco
