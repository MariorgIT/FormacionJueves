# Definición de una función para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Solicitar al usuario que ingrese un número entero positivo
num = int(input("Ingrese un número entero positivo: "))

# Verificar si el número ingresado es positivo
if num < 0:
    print("Mira que te he dicho entero positivo que eres tontísimo.")
elif num == 0:
    print("El factorial de 0 es 1, resultado abajo")
else:
    print("El factorial de", num, "es", factorial(num))


print("Cambio Andrés")