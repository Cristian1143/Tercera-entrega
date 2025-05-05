# Programa para determinar cuál número es mayor y cuál es menor

# Pedimos al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Comparamos los dos números
if numero1 > numero2:
    print("El mayor es:", numero1)
    print("El menor es:", numero2)
elif numero2 > numero1:
    print("El mayor es:", numero2)
    print("El menor es:", numero1)
else:
    print("Ambos números son iguales.")
