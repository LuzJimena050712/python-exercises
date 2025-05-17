#Creación de un diccionario:
d1={"Nombre": "Samanta","Edad":27,"Dirección":"Tepeji", "e_mail": "sama@.gmail.com"}
d2={"Nombre": "Maria","Edad":30,"Dirección":"Tula Hgo", "e_mail": "maria35@.gmail.com"}
d3={"Nombre": "José","Edad":25,"Dirección":"Jilotepec", "e_mail": "pepe@.gmail.com"}

#Imprimir diccionario completo:
print(d1)
print(d2)
print(d3)

#Imprimir un solo dato:
print(d1['Nombre'])

#Usando un get:
print(d1.get('Dirección'))

#Modificar un elemento usar []:
d2['Nombre'] = "Laura"
print(d2)    

#Si el key no existe lo añade:
d1['CP'] = 54240
print(d1)

#Devolveer los valores del diccionario: values()
print(list(d1.values()))

#   Elimina cualquier elemento: pop()
salida=d1.pop('Edad')
print(d1)

#Llamar un diccioanrio y tiene como entrada otro diccionario: update

t1={"a": 100, "b":200}
t2={"e":50, "d": 400}

t1.update(t2)
print(t1)

#Imprimir fecha del equipo:

from datetime import datetime
fecha=datetime.now()
print (fecha)

#Otra manera:

import datetime
fecha=datetime.datetime.now()
print (fecha)

#Visualizar unicamente el año:
año=datetime.datetime.strftime(fecha, "%Y"+ "-" + "%m")
print(año)

#%d dia
#%m mes
#%Y año
#%H hora
#%M minutos
#%S segundos

