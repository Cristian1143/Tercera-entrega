# Programa para sumar los cuadrados de los 100 primeros números naturales

# Inicializamos la variable que guardará la suma total
suma_cuadrados = 0

# Usamos un bucle para recorrer los números del 1 al 100
for numero in range(1, 101):
    suma_cuadrados += numero ** 2  # Sumamos el cuadrado del número actual

# Mostramos el resultado final
print("La suma de los cuadrados de los 100 primeros números naturales es:", suma_cuadrados)
