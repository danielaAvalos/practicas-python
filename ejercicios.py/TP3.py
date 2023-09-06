#BUCLES repetir hasta que la condicion a cumplir sea verdadera utiliza while
"""
PRIMERO armamos un esquema del ejercicio y SEGUNDO pasamos todo a while 

5.	Escriba un programa para obtener el grado de eficiencia de un operario de una fábrica de tornillos,
 de acuerdo a las siguientes dos condiciones que se le imponen para un período de prueba: 

a.	• Producir menos de 200 tornillos defectuosos. 
b.	• Producir más de 10000 tornillos sin defectos. 

• El grado de eficiencia se determina de la siguiente manera: 

1.	• Si no cumple ninguna de las condiciones, grado 5. /
2.	• Si sólo cumple la primera condición, grado 6. /
3.	• Si sólo cumple la segunda condición, grado 7. 
4.	• Si cumple las dos condiciones, grado 8

lo que debo hacer en los puntos 1, 2, 3, 4, 5 es variable para los tornillos defectuosos
variable para los tornillos perfectos
if

#PRIMER esquema sin while 
tornillo_defectuoso = int(input("Ingrese la cantidad de tornillos defectuosos que hizo el operario: ")) #puntos 5 a 
tornillo_perfecto = int(input("Ingrese la cantidad de tornillos perfectos que hizo el operario: ")) #puntos 5 b
if tornillo_defectuoso > 200 and tornillo_perfecto < 10000: #puntos 5 a,b 
    print("El operario es de grado 5") #puntos 1
elif tornillo_defectuoso <= 200 and tornillo_perfecto <10000: #puntos 2
    print("El operario es de grado 6") 
elif tornillo_defectuoso > 200 and tornillo_perfecto >= 10000: #puntos 3
    print("El operario es de grado 7")
else:
    print("El operario es de grado 8")
    
#Segundo esquema con while
numero = int(input("Ingrese un numero: "))
while numero != 0:
    print("No adivino el numero")
    numero = int(input("Ingrese otro numero: "))
print("Adivinaste")
"""

#Actividad, una profesora quiere cargar las notas de sus alumnos 

"""nota1 = int(input("Ingrese la primera nota del alumno: "))
nota2 = int(input("Ingrese la segunda nota del alumno: "))
nota3 = int(input("Ingrese la tercera nota del alumno: "))
promedio = (nota1 + nota2 + nota3) / 3 #este codigo es para cada alumno que tengo 

#para esto se utiliza bucle para cantidades grandes 
from optparse import AmbiguousOptionError


contador = 0 #contadores cuenta las vueltas, tiene que estar si o si o no me va dejar de ejecutar nunca
alumno = {} #diccionario
alumnos = [] #lista
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
while cantidad_alumnos > contador: #contador cuenta las vueltas, si o si tiene que estar o no va de dejar de ejecutar 
    contador += 1
    nombre_alumno = input("Ingrese el nombre del alumno: ") 
    nota1 = int(input("Ingrese la primera nota del alumno: "))
    nota2 = int(input("Ingrese la segunda nota del alumno: "))
    nota3 = int(input("Ingrese la tercera nota del alumno: "))
    promedio = (nota1 + nota2 + nota3) / 3
    alumno = {"nombre":nombre_alumno, "promedio":promedio} #alumno representado en diccionario 
    alumnos.append(alumno)                       #y ese diccionario guardado en una lista total

lista = [1, 2, 3, 4, 5, 6] #el valor lista va tomar un numero, lo va a imprimir y sale del bucle
for valor_lista in lista: #for para recorrer nuestra lista
    print(valor_lista)
 """
 
 
 
 
 
cantidad_registros = int(input("Ingrese la cantidad de empleados: "))
contador = 0
empleada = {}
empleadas = []
while contador < cantidad_registros:
    nombre_empleada = input("Ingrese el nombre de la empleada: ")
    tornillo_defectuoso = int(input("Ingrese la cantidad de tornillos defectuosos que hizo el operario: ")) #puntos 5 a 
    tornillo_perfecto = int(input("Ingrese la cantidad de tornillos perfectos que hizo el operario: ")) #puntos 5 b
    if tornillo_defectuoso > 200 and tornillo_perfecto < 10000: #puntos 5 a,b 
        grado = 5   #ponemos este condicional para la variable 5 y la va concatenar
        print(f"El operario es de grado {grado}") #puntos 1 #para concatenar f y {}
    elif tornillo_defectuoso <= 200 and tornillo_perfecto <10000: #puntos 2
        grado = 6
        print(f"El operario es de grado {grado}") 
    elif tornillo_defectuoso > 200 and tornillo_perfecto >= 10000: #puntos 3
        grado = 7
        print(f"El operario es de grado {grado}")
    else:
        grado = 8
        print(f"El operario es de grado {grado}")
    contador += 1
    empleada = {"nombre":nombre_empleada, "grado":grado} #diccionario
    empleadas.append(empleada) #lista

for empleadaaa in empleadas: #esto no se hace pero se pone para llamar otro cosa que no sea diccionario y lista 
    print(empleadaaa)









#BUCLES declarar un rango numerico de veces repetir, ejecute verdadero y finalice falso utiliza for in