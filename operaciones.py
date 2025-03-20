# Salguero López Santiago José María 
def suma(a: int, b: int) -> int:
    if a is None or b is None:
        return None
    return a + b

def resta(a: int, b: int) -> int:
    if a is None or b is None:
        return None
<<<<<<< HEAD
    return a - b

=======
    return a - b   
>>>>>>> 4454f3238f68c5b63bf12237576f4f3679f3eabc

def menu():
    while True:
        print("\nMenú de Operaciones")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                a = int(input("Ingrese el primer número: "))
                b = int(input("Ingrese el segundo número: "))
                resultado = suma(a, b)
                print(f"El resultado de la suma es: {resultado}")
            except ValueError:
                print("Error: Ingrese solo números enteros.")
<<<<<<< HEAD

=======
>>>>>>> 4454f3238f68c5b63bf12237576f4f3679f3eabc
        if opcion == "2":
            try:
                a = int(input("Ingrese el primer número: "))
                b = int(input("Ingrese el segundo número: "))
                resultado = resta(a, b)
                print(f"El resultado de la resta es: {resultado}")
            except ValueError:
<<<<<<< HEAD
                print("Error: Se a generado un error, vuelva a intentarlo.")

=======
                print("Error: Ingrese solo números enteros.")   
        
>>>>>>> 4454f3238f68c5b63bf12237576f4f3679f3eabc
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
