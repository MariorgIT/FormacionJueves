# Definición de una función para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
    
aaa
# Solicitar al usuario que ingrese un número entero positivo
num = int(input("Ingrese un número entero positiv bbbo: "))

# Verificar si el número ingresado es positivo
if num < 0:
    print("El factorial no está definidccco para números negativos.")
elif num == 0:
    print("El factorial de 0 es 1")
else:
    print("El factorialddd de", num, "es", factorial(num))