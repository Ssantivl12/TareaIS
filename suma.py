ef suma(a, b):
    """
    Función que recibe dos números y devuelve su suma.
    """
    return a + b

# Ejemplo de uso
if __name__ == "__main__":
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = suma(num1, num2)
    print(f"La suma de {num1} y {num2} es: {resultado}")
