"""
#las listas si o si se tienen que declarar con los corchetes
#alumnos =  ["leo", "sandra",13 ]
#print(type(alumnos))

#creamos una lista
lista_de_supermercado =  ["Fideos", "Cervezas", "Queso", "Sal", "Cafe", "Milanesas"]
print(lista_de_supermercado)
lista_de_supermercado.append("Gaseosa")#el append agraga un elemento al final 

print(lista_de_supermercado)

#el metodo insert pide el valor del indice donde ingresar los datos
lista_de_supermercado.insert(2,"Azucar")
print(lista_de_supermercado)

#metodos para borrar datos de la lista
print(lista_de_supermercado)
lista_de_supermercado.remove("Sal") #el metodo remove nos pide el dato que quermos borrar
print(lista_de_supermercado)

#metodo pop (para borrar)
#lista_de_supermercado.pop(0) #pop nos pide el valor del indice que queramos borrar
print(lista_de_supermercado)
lista_de_supermercado.pop() #si no se ingresa un valor, borra el ultimo elemento de lista 
print(lista_de_supermercado)
lista_de_supermercado.insert(0, "jugo")
print(lista_de_supermercado)
lista_de_supermercado.pop()
print(lista_de_supermercado)

#metodo para borrar clear
#lista_de_supermercado.clear() #borra solo los datos que tiene en el interior 
print(lista_de_supermercado)

print(lista_de_supermercado.index("Cerveza"))


#vamos a declarar nuestro primer diccionario 
celulares =  {"Marca":"Samsung", "Modelo":"a50", "Color":"Negro"},  {"Marca":"Motorola", "Modelo":"G8", "Color":"Azul"}
print(celulares)

print(celulares.get("Color")) #busca el valor de una llave 

print(celulares.keys())       #metodos keys nos trae todas las llaves

celulares.update({"RAM":"12GB"}) #metodo update agregamos un elemento al diccionario 
print(celulares)

#vamos a borrar una llave del diccionario
celulares.pop("Modelo")         #cualquier llave que se ingrese la va a eliminar  
print(celulares)

#celulares.pop()                 #siempre nos va a pedir que llave vamos a borrar 
print(celulares)

#tenemos el metodo popitem. SI NOS VA A BORRAR NUESTRO ULTIMO ELEMENTO
celulares.popitem()
print(celulares)

celulares.popitem()
print(celulares)

#creamos la variable a evaluar 
contraseña_guardada = "123456"

#ingresar la contraseña con la que vamos a comparar 
contra = input("Ingrese la contraseña: ")
#condicion
if contra == contraseña_guardada:
    #en caso de que sea verdadero ejecuta esta parte
    print("Bienvenido!!!")
else:
    #en caso de que sea falso, ejecuta esta otra
    print("contraseña incorrecta")


#vamos a declarar multiples condiciones

nota = int(input("Ingrese la nota: "))
asistencia = int(input("Ingrese la asistencia: "))
#condicion 1
if nota >= 7 and asistencia >25:
    print("El alumno esta aprobado")
#segunda condicion
elif nota > 4 and asistencia <= 20:
    print("El alumno no esta aprobado")
#si es falso el elif
else:
    print("El alumno tiene que recursar")
"""

#vamos a ver que distancia hay entre el planeta tierra y la luna 

"""distancia = 384400 #km
distancia_ingresada = int(input("Ingrese la distancia que crea que hay entre la tierra y la luna: "))
while distancia != distancia_ingresada: 
    print("No acertaste, intenta de nuevo")
    distancia_ingresada = int(input("Ingrese el numero que crea que es: "))

print("Acertaste!!!")
"""
lista = [14, 5, 7, 9, 85, 89, ["Leo", "Fede", "Flor"]]
print(lista)

for items in lista:
    print(items)