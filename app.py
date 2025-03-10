# calculo del indice de masa corporal paso a paso de lo facil a la forma pro

# estas son las categorias de peso segun el indice de masa corporal
# IMC = peso / altura^2
# si es menor de 18.5 esta bajo de peso
# si esta entre 18.5 y 24.9 esta en peso normal
# si esta entre 25 y 29.9 esta en sobrepeso
# si esta entre 30 y 34.9 esta en obesidad tipo 1
# si esta entre 35 y 39.9 esta en obesidad tipo 2
# si es mayor de 40 esta en obesidad tipo 3

# peso = float(input("Ingresa tu peso en kg: "))
# altura = float(input("Ingresa tu altura en metros: "))

# imc = peso / altura**2
# print("Tu indice de masa corporal es: ", imc)


# def calcular_imc(peso, altura):
#     return peso / altura**2

# def main():
#     print("Calculadora del indice de masa corporal")
#     peso = float(input("Ingresa tu peso en kg: "))
#     altura = float(input("Ingresa tu altura en metros: "))
#     imc = calcular_imc(peso, altura)
#     print("Tu indice de masa corporal es: ", imc)

#     if imc < 18.5:
#         print("Estas bajo de peso")
#     elif imc < 24.9:
#         print("Estas en peso normal")
#     elif imc < 29.9:
#         print("Estas en sobrepeso")
#     elif imc < 34.9:
#         print("Tienes obesidad tipo 1")
#     elif imc < 39.9:
#         print("Tienes obesidad tipo 2")
#     else:
#         print("Tienes obesidad tipo 3")

# if __name__ == "__main__":
#     main()


import tkinter as tk
from tkinter import messagebox

def calcular_imc(peso, altura):
    return peso / altura**2

def calcular():
    try:
        peso = float(peso_entry.get())
        altura = float(altura_entry.get())
        imc = calcular_imc(peso, altura)
        label_resultado.config(text="Tu indice de masa corporal es: " + str(imc))

        if imc < 18.5:
            messagebox.showinfo("Resultado", "Estas bajo de peso")
        elif imc < 24.9:
            messagebox.showinfo("Resultado", "Estas en peso normal")
        elif imc < 29.9:
            messagebox.showinfo("Resultado", "Estas en sobrepeso")
        elif imc < 34.9:
            messagebox.showinfo("Resultado", "Tienes obesidad tipo 1")
        elif imc < 39.9:
            messagebox.showinfo("Resultado", "Tienes obesidad tipo 2")
        else:
            messagebox.showinfo("Resultado", "Tienes obesidad tipo 3")
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numericos")

root = tk.Tk()
root.title("Calculadora de IMC")

resultado = tk.Label(root, text="Peso en (kg):")
resultado.pack()
peso_entry = tk.Entry(root)
peso_entry.pack()

label_altura = tk.Label(root, text="Altura en (m):")
label_altura.pack()
altura_entry = tk.Entry(root)
altura_entry.pack()

boton_calcular = tk.Button(root, text="Calcular IMC", command=calcular)
boton_calcular.pack()

label_resultado = tk.Label(root, textvariable=resultado)
label_resultado.pack()

label_clasificacion = tk.Label(root, text="Clasificacion:")
label_clasificacion.pack()

root.mainloop()