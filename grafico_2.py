import tkinter as Tk
from tkinter import messagebox

def suma():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingrese números válidos")

def resta():
    try:
        num1 = int(entry_num1.get())
        num2 =int(entry_num2.get())
        resultado = num1 - num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingrese números válidos")

def multiplica():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        resultado = num1 * num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingrese números válidos")

def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            raise ZeroDivisionError
        resultado = num1 / num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingrese números válidos")
    except ZeroDivisionError:
        messagebox.showerror("Error matemático", "La división por cero no está permitida")

# Crear la ventana principal
app = Tk.Tk()
app.title("CALCULADORA BÁSICA")

# Crear y colocar los widgets
Tk.Label(app, text="PRIMER NÚMERO:").pack()
entry_num1 = Tk.Entry(app)
entry_num1.pack()

Tk.Label(app, text="SEGUNDO NÚMERO:").pack()
entry_num2 = Tk.Entry(app)
entry_num2.pack()

label_resultado = Tk.Label(app, text="RESULTADO: ")
label_resultado.pack()

Tk.Label(app, text="").pack()
Tk.Button(app, text="SUMA", command=suma).pack()
Tk.Label(app, text="").pack()
Tk.Button(app, text="RESTA", command=resta).pack()
Tk.Label(app, text="").pack()
Tk.Button(app, text="MULTIPLICACIÓN", command=multiplica).pack()
Tk.Label(app, text="").pack()
Tk.Button(app, text="DIVISIÓN", command=divide).pack()

# Configurar la geometría de la ventana
app.geometry("500x500")

# Ejecutar la aplicación
app.mainloop()
