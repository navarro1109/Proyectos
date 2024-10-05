#los constructores se definen con __init__()

print("Hola")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar (self):
        print("Hola", self.nombre, ", tu tienes", self.edad, "años")
      
      #self significa una instancia que accede a cada dato

nombre = input("cual es tu nombre?\n")
edad = input("que edad tienes\n")
edad = int(edad)

persona1 = Persona(nombre, edad)
persona2 = Persona("Daniel", 17)

persona1.saludar()


    