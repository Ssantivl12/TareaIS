import math

def logaritmo(x, base=10):

 #    Kevin John Calderon Mamani.
    
    if x <= 0:
        raise ValueError("El número debe ser positivo.")
    if base <= 0 or base == 1:
        raise ValueError("La base debe ser positiva y diferente de 1.")

    # Calcular el logaritmo usando la función math.log
    resultado = math.log(x, base)
    return resultado

# Llamada a la función
if __name__ == "__main__":
    numero = 100
    base = 10
    try:
        resultado = logaritmo(numero, base)
        print(f"El logaritmo de {numero} en base {base} es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")