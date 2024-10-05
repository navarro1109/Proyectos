class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        base = float(base)
        altura = float(altura)
        
    def area (self):
        return self.base * self.altura
        
    def perimetro (self):
        return ((self.base + self.altura)*2)
        
      
      #self significa una instancia que accede a cada dato


solucion1 = Rectangulo(5, 3)

solucion1.area()
solucion1.perimetro()

print("Area: ", solucion1.area())
print("Perimetro: ", solucion1.perimetro())