#armamos una lista “Animales” [], 

contador = 0
animales = []
animal = {}
animales = ["jirafa", "elefante", "tigre", "mono"]
print(animales)
cantidad_animales = int(input("Insertar cantidad de animales: "))
while contador < cantidad_animales:
    nombre_animal = input("Ingrese un animal: ")
    animal_extinto = int(input("Ingrese la cantidad de animales extinto: "))
    fuera_de_peligro_de_extincion = int(input("Ingrese la cantidad de animales fuera de peligro de extincion: "))
    en_vias_de_extincion = int(input("Ingrese la cantidad de animales en vias de extincion: "))
    if animal_extinto < 0 and fuera_de_peligro_de_extincion < 10000:
        print("animal fuera de peligro de extincion")
    elif animal_extinto >= 0 and fuera_de_peligro_de_extincion > 10000:
        print("animal extinto")
    if en_vias_de_extincion  > 10000 and fuera_de_peligro_de_extincion > 10000:
        print("en vias de extincion")
    elif en_vias_de_extincion >= 10000 and fuera_de_peligro_de_extincion < 10000:
        print("fuera de peligro de extincion")
    else:
        print("la poblacion actualmente de animales se extinguio")
        
