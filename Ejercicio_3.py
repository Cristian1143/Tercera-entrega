# Programa para convertir euros a dólares

# Definimos la tasa de cambio (ejemplo: 1 euro = 1.10 dólares)
tasa_cambio = 1.10

# Pedimos al usuario que ingrese la cantidad en euros
euros = float(input("Ingrese la cantidad en euros: "))

# Realizamos la conversión
dolares = euros * tasa_cambio

# Mostramos el resultado
print("La cantidad equivalente en dólares es:", dolares)
17