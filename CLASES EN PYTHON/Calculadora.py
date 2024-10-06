class Calculadora:
  def __init__(self, num1, num2):
      num1 = float(num1)
      num2 = float(num2)
      self.num1 = num1
      self.num2 = num2

  
  def sumar(self):
      return self.num1 + self.num2


  def restar(self):
      return self.num1 - self.num2


  def multiplicar(self):
      return self.num1 * self.num2  
  
  def dividir(self):
      if self.num2 == 0:
          return "No se puede dividir por 0"
      return self.num1 / self.num2

print("Calculadora")
num1 = input("Ingrese el primer numero: \n")
num2 = input("Ingrese el segundo numero: \n")
calculadora = Calculadora(num1, num2)

print(num1, "+", num2, "=", calculadora.sumar())
print(num1, "-", num2, "=", calculadora.restar())
print(num1, "*", num2, "=", calculadora.multiplicar())
print(num1, "/", num2, "=", calculadora.dividir())