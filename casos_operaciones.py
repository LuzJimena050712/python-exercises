a= int(input("Ingresa el primer numero:"))
b= int(input("Ingresa el segundo numero:"))

print ("{+} suma a+b")
print ("{-} resta a+b")
print ("{*} multiplica a*b")
print ("{/} divide a/b")

simbolo= input("Ingresa la operación insertando el simbolo: ")
match simbolo:
    case "+":
        print ("El resultado", (a+b))
    case "-":
        print ("El resultado", (a+b))
    case "*":
        print ("El resultado", (a*b))
    case "/":
        if b!=0:
            print ("El resultado", (a/b))
        else: 
           print("No se puede dividir entre cero.")
    case _:
        print("Operación invalida")