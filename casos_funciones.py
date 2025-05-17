acu=0
while True: # al menos una  vez se ejecutara
    n1=(input("Teclea el número / o presiona x para salir del programa"))
    if (n1== "x"):
        break #rompe el ciclo
    else:
        acu=acu + int (n1) # toma n1 como entero
        # esta fuera del ciclo lo siguiente
if (acu>=0):
    print(" El resultado  final del acomulador es: ", acu)
else:
    print("Se pulso x para salir de bucle")