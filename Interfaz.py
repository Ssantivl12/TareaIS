import tkinter as tk
from tkinter import simpledialog

# Funciones para las operaciones matemáticas
def suma():
    num1 = simpledialog.askfloat("Entrada", "Ingrese el primer número:")
    num2 = simpledialog.askfloat("Entrada", "Ingrese el segundo número:")
    #resultado = num1 + num2
    #label_resultado.config(text=f"Resultado: {resultado}")

def resta():
    num1 = simpledialog.askfloat("Entrada", "Ingrese el primer número:")
    num2 = simpledialog.askfloat("Entrada", "Ingrese el segundo número:")
    #resultado = num1 - num2
    #label_resultado.config(text=f"Resultado: {resultado}")

def multiplicacion():
    num1 = simpledialog.askfloat("Entrada", "Ingrese el primer número:")
    num2 = simpledialog.askfloat("Entrada", "Ingrese el segundo número:")
    #resultado = num1 * num2
    #label_resultado.config(text=f"Resultado: {resultado}")

def division():
    num1 = simpledialog.askfloat("Entrada", "Ingrese el primer número:")
    num2 = simpledialog.askfloat("Entrada", "Ingrese el segundo número:")
   # if num2 == 0:
    #    label_resultado.config(text="Error: División por cero")
    #else:
     #   resultado = num1 / num2
      #  label_resultado.config(text=f"Resultado: {resultado}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Sencilla")

# Establecer el tamaño de la ventana y el color de fondo
ventana.geometry("500x400")  # Ancho x Alto
ventana.config(bg="#f5f5dc")  # Fondo color crema (beige)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado:", font=("Arial", 18), width=40, height=3, anchor="w", relief="solid", bg="white")
label_resultado.pack(pady=20)

# Frame para los botones
frame_botones = tk.Frame(ventana, bg="#f5f5dc")  # Fondo color crema
frame_botones.pack()

# Botones para las operaciones
btn_suma = tk.Button(frame_botones, text="Suma", width=15, height=2, command=suma)
btn_suma.grid(row=0, column=0, padx=10, pady=10)

btn_resta = tk.Button(frame_botones, text="Resta", width=15, height=2, command=resta)
btn_resta.grid(row=0, column=1, padx=10, pady=10)

btn_multiplicacion = tk.Button(frame_botones, text="Multiplicación", width=15, height=2, command=multiplicacion)
btn_multiplicacion.grid(row=1, column=0, padx=10, pady=10)

btn_division = tk.Button(frame_botones, text="División", width=15, height=2, command=division)
btn_division.grid(row=1, column=1, padx=10, pady=10)

# Ejecutar la ventana
ventana.mainloop()