import tkinter as Tk

def suma ():
    num1= int(entry_num1.get()) 
    num2= int (entry_num2.get())
    resultado=num1+num2
    label_resutado.config(text="resultado" + str (resultado))

app = Tk.Tk()
app.title("TECNOLOGICO DE ESTUDIOS SUPERIORES DE JILOTEPEC")
label_num1=Tk.label(text = "primer numero")
label_num1=Tk.entry()

label_num2=Tk.label(text = "segundo numero")
label_num2=Tk.entry()

label_resutado = Tk.label(text = "*****")
button_suma= Tk.button (text = "suma", comand=suma)

label_num1.pack()
entry_num1.pack()

label_num2.pack()
entry_num2.pack()

label_resutado.pack()
button_suma.pack()

app.geometry("500x500")
app.mainloop