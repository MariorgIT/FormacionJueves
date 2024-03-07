# Definición de una funclar el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Solicitar al usuario que ingrese un número entero positivo
num = int(input("Ingrese un número entero positivo: "))

# Verificar si el número ingresado es positivo
if num < 0:
    print("El factorial no está definido para números negativos.")
elif num ==
    print("El facto)
else:
    print("El factorial de", num, "es", factorial(num))