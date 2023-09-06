"""""
#ingresamos un dato
input()

#declarando una variable e ingresamos el valor por teclado
nombre = input("Ingrese su nombre: ")

#imprimiendo bienvenido mas nuestra variable
print("Bienvenido ", nombre)

#declaramos mas variables 
dia = "Lunes"
curso = "python"
turno = "noche"

#print("hoy es", dia, "El curso es de" , curso, "el turno es", turno) #Estamos concatenando
print(f"Hoy es{dia} Nuestro curso es el de{curso} y estamos en el turno{turno}") #es recomendable usar la concatenando
#con f asi no nos volvemos locos con la coma

#variable con mayuscula
Dia = "Martes"
print(Dia)

#variable todo ingresando con mayuscula es una CONSTANTE
DIA = "Miercoles"
print(DIA)

#variable CAMEL CASE
AlumnosDelCursoPython = 73

#variable tipo SNAKE KASE
alumnos_del_curso_python = 74
"""
#VAMOS A DECLARAR 2 VARIABLES PARA HACER OPERACIONES MATEMATICAS
"""num1 = 50
num2 = int(input("Ingrese el segundo numero: ")) #int para convertir el ingreso por pantalla de tipo string a entero 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)

#vamos a asignar una suma a una nueva variable 
num3 = num1 + num2
#num3 = 90
#num3 = 90 * 2
num3 = num3 * 2 
print(num3)
#print(num4)
NUM = 1000
print(NUM)
NUM = 5 #si declaramos una variable con mayuscula o minuscula y la llamamos en el print tiene que ser igual 
print(num) #a como este declarada """

#vamos a declar nuestra primer tupla
#las tuplas siempre comienzan en 0
"""persona = ("Leonel", "Bs As", "Python", "Turno noche")
print(persona[0], persona[2])
#metodo len que nos muestra cuantos datos hay ingresados en nuestra tupla
print(len(persona))
#index es un metodo nos muestra la posicion donde se encuentra un valor especifico
print(persona.index("Bs As"))
"""
#Tupla anidada por 3 tuplas dentro de una
cursos = (("Python", "Turno noche", 65),("CSS","Turno tarde", 40), ("HTML", "Turno mañana", 50))
#print(cursos)

#Mostrar un dato especifico dentro de una tupla anidada
#print(cursos[1])

#Mostrar un dato especifico de la tupla dentro de otra tupla
#print(cursos[2][1]) #[2]es la tupla HTML y el [1] es la posicion de turno mañana 
print(cursos[2][1], cursos[0][1])

