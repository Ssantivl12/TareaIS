#jhonny rocha almendras
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Ingresa la cantidad de términos: "))
fibonacci(n)
