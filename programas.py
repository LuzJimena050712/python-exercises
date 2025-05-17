
def uno():
    x=int(input("Dime que table de multiplicar deseas ejecutar:"))
    a=1;
    while a <= 10: #ciclo.
        print (f"{x} * {a} = {x*a}") #f imprime un mensaje formateado.
        a+=1

def dos():
    n1=int(input("Dame un número"))
    if n1%2==0:
        print("El número es par")

    else:
        print("El número es impar")

def tres():
    n1=int(input("Ingresa  tu calificación:"))
    if n1==100:
        print ("¡Excelente felicidades!")
    elif n1<=99 and n1>=90:
        print ("¡Muy bien!")
    elif n1<=89 and n1>=80:
        print ("¡Bien!")
    elif n1<=79 and n1>=70:
        print ("Alumno regular")
    else:
        print ("Alumno no aprobado")

def cuatro():
    x=int(input ("Ingresa un numero: "))
    a=1
    suma=0
    while a<=x:
        b = 2
        while b<x+2:
            c = pow(a,b)
            suma = suma+c
            resultado = suma/x
            a = a+1
            b = b+1
        print ("El resultado es: ", resultado)

def cinco():
    año=2024
    print ("1 Si vienes de otra escuela (Febrero)")
    print ("2 Admisión Tesji ")

    p= input("Ingresa el número que corresponda segun tu caso:")
    match p:
        case "1":
            print (1)
        case "2":
            print (2)
        case _:
            print("Opción invalida")
            p= input("Ingresa el número que corresponda segun tu caso:")
    match p:
        case "1":
            print (1)
        case "2":
            print (2)

    print ("{1}IngenierÍa Industrial")
    print ("{2}IngenierÍa en TIC'S")
    print ("{3}Ingeniería en Sistemas Computacioanles")
    print ("{4} Ingenería Química")
    print ("{5}Ingeniería Civil")
    print ("{7} Ingenería Eléctrica")
    print ("{8} Ingenieria Logistica")
    print ("{9} Licenciatura en Admisnistración")

    c= input ("Ingresa el número según corresponda tu carrera:")
    match c:
        case "1":
            print (1)
        case "2":
            print (2)
        case "3":
            print (3)
        case "4":
            print (4)
        case "5":
            print (5)
        case "6":
            print (6)
        case "7":
            print (7)
        case "8":
            print (8)
        case "9":
            print (9)
        case _:
            print ("Opción invalida")

    b= int(input("Ingresa tu número de alumno:"))

    if b<10:
        x="00"
        z=str(x)+ str(b)
        print(z)

    elif b<100 and b>=10:
        x="0"
        z=str(x)+ str(b)
        print(z)
    elif b>=100 and b<=999:
        z=str(b)
    elif b==0:
        print("Opción invalida")
        
    else:
        print("Opción invalida")

    concatenar=str(año)+str(p)+str(c)+str(z)
    print ("La matricula es: ", concatenar)


while True:
    print("1.-x tabla")
    print("2.-Par o impar")
    print("3.-If anidado")
    print("4.-Formula")
    print("5.-Número control")
    print("6.-Salir")
    x= (input("Ingrese la opción que desee: "))

    if (x== "6"):
        break
    else:
        match x:
            case "1":
                uno()
            case "2":
                dos()
            case "3":
                tres()
            case "4":
                cuatro()
            case "5":
                cinco()
            case _:
                print("Opción Invalida :(")