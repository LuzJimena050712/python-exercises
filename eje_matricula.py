import sys
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
        sys.exit()
        
    
   
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
        sys.exit()

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
    sys.exit()
else:
    print("Opción invalida")
    sys.exit()

concatenar=str(año)+str(p)+str(c)+str(z)
print ("La matricula es: ", concatenar)