""""
la diferencia entre clase y objeto es que clase es nuestro model y nuestro objeto es plastilina (es un ejemplo)
Usamos tambien clase para ahorrar codigo 
"""
class Auto():
    def __init__(self, color, marca, combustible):     #iniciarlizar sus atributos __init__ 
        self.color = color                             #self es para que no tengamos que escribir auto1,auto2...
        self.marca = marca
        self.combustible = combustible 
    
    def __str__(self):       #para que devuelva uno de los self hay que poner __str__
        return self.marca
    
    #si quiero retornar 2 cosas 
    def __str__(self):
        return f"{self.marca} {self.color}"
    
    def __str__(self):
        return f"{self.marca} {self.color} {self.combustible}"
    
    #para que el usuario pueda acceder a los de mas atributos de mi objeto, get que significa obtener o mostrar
    def get_color(self):
        return self.color
    
    
    """#actualizar
    def actualizar_combustible(self, combustible):
        self.combustible = combustible
        return self.combustible """
    #actulizar con buena practica, set
    def set_combustible(self, combustible):
        self.combustible = combustible
        return self.combustible
        
        
        
color = "verde"   
auto1 = Auto(color, "ford", "nafta")
print(auto1)
combustible = "GNC"
auto1.set_combustible(combustible)
"""auto1.actualizar_combustible(combustible)
print(auto1)"""
print(auto1.get_color())
print(auto1)

