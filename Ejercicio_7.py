# Función que implementa el algoritmo de Euclides
def gcd(a, b):
    while b != 0:  # Mientras b no sea 0
        a, b = b, a % b  # Reemplazamos a por b y b por el residuo de a / b
    return a  # Cuando b es 0, a contiene el GCD

# Pedimos al usuario que ingrese dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Calculamos el GCD utilizando la función
resultado = gcd(numero1, numero2)

# Mostramos el resultado de forma simple, como en el ejemplo original
print("El GCD de", numero1, "y", numero2, "es:", resultado)
