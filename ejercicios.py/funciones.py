#funciones es un metodo para evitar repetir porciones o lineas de codigo y se utiliza def
#las funciones nos permitieron replicar un codigo varias veces, sin la necesidad de volver a escribirlo.
#pero no siempre el resultado final de la funcion va ser el mismo, podemos asignarle un valor a la funcion para que sea utilizado dentro.
#datos o variables usamos dentro de una funcion 

from functools import total_ordering


def suma(numero): #def siempre va arriba para que python vea que existe una funcion, para python la funcion existe despues de la linea 10 
    numero1 = int(input("Ingrese otro numero para sumar: "))
    total = numero + numero1  #no importa cuanto veces invoque para a bajo siempre me va sumar
    return f"El resultado de {numero} + {numero1} = {total}" #cuando tenemos varios resultados podemos pedir a la funcion que nos retorne uno o mas valores, return
    
def resta(numero):
    numero1 = int(input("Ingrese otro numero para restar: "))
    return numero - numero1 
  
def multiplicacion(numero):
    numero1 = int(input("Ingrese otro numero para multiplicar: "))
    total = numero * numero1
    return f"El resultado de {numero} * {numero1} es = {total}"

def division(numero):
    numero1 = int(input("Ingrese otro numero para dividir: "))
    if numero1 == 0:    #en el caso que quieran dividir por cero se hace esto 
        return f"El numero {numero} no se puede dividir por {numero1}"
    else:
        total = numero / numero1
        return f"El resultado de {numero} / {numero1} es = {total}"
    
numero = int(input("Ingrese un numero: "))
operador = input("Ingrese el operador a utilizar: ")
if operador == "+":     # los dos puntos es un operador que corta parte de un objeto de secuencia como lista, tupla o cadena
    print(suma(numero))
elif operador == "-":
    print(resta(numero))
elif operador == "*":
    print(multiplicacion(numero))
elif operador == "/":
    print(division(numero))