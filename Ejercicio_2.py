# Programa para sumar los 100 números siguientes a un número ingresado

# Solicitar al usuario que ingrese un número entero
numero_inicial = int(input("Ingrese un número entero: "))

# Inicializamos la variable para almacenar la suma
suma_total = 0

# Usamos un bucle para sumar los 100 números siguientes
for i in range(1, 101):  # Desde 1 hasta 100
    suma_total += numero_inicial + i

# Mostramos el resultado
print("La suma de los 100 números siguientes es:", suma_total)
