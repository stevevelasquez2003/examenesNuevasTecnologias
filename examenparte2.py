def calcular_factorial(n):
    factorial = lambda f, x: 1 if x == 0 else x * f(f, x - 1)
    return factorial(factorial, n)


numero = 5
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es {resultado}")
