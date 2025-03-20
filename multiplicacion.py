#Gonzales Tincuta Josue Arturo
def multiplicacion(a: float, b: float) -> float:
    return a * b

if __name__ == "__main__":
    try:
        input("Funcion de Multiplicar\nHecho por Josue Arturo Gonzales Tincuta")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        resultado = multiplicacion(num1, num2)
        print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    except ValueError:
        print("Error: Por favor, ingrese solo números válidos.")
