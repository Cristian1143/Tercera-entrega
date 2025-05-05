# Programa para mostrar los números impares menores al número ingresado

# Pedimos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Mostramos todos los impares menores que ese número
print("Números impares menores que", numero, ":")

for i in range(1, numero):
    if i % 2 != 0:
        print(i)
