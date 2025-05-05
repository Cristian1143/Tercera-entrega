import math  # Importamos la biblioteca math para usar sqrt

# Pedimos al usuario los coeficientes de la ecuación
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Verificamos si es una ecuación de segundo grado válida
if a == 0:
    print("No es una ecuación de segundo grado.")
else:
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c

    # Evaluamos el discriminante para ver qué tipo de soluciones tiene
    if discriminante > 0:
        # Dos soluciones reales diferentes
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("La ecuación tiene dos soluciones reales diferentes:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif discriminante == 0:
        # Una solución real doble
        x = -b / (2*a)
        print("La ecuación tiene una solución real doble:")
        print("x =", x)
    else:
        # No hay soluciones reales
        print("La ecuación no tiene soluciones reales.")
