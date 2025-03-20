#Magner Jhoan Orellana Montaño
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."

numerador = float(input("Ingresa el numerador: "))
denominador = float(input("Ingresa el denominador: "))

resultado = dividir(numerador, denominador)

print(f"El resultado de la división es: {resultado}")
