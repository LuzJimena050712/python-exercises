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