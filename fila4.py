# Definición de una función para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Solicitar al usuario que ingrese un número entero positivo
num = int(input("Ingrese un número entero positivo: "))
