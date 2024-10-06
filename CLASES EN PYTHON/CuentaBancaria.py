class CuentaBancaria:
  def __init__(self, titular, saldo):
      saldo = float(saldo)
      
      self.titular = titular
      self.saldo = saldo
    
  
  def depositar(self, cantidad):
      cantidad = float(cantidad)
      self.saldo += cantidad
  
  def retirar(self, cantidad):
      cantidad = float(cantidad)
      if cantidad <= self.saldo:
          self.saldo -= cantidad
      else:
          print('Fondos insuficientes')

  def mostrar_saldo(self):
    print('Titular:',  self.titular, '\n')
    print('Saldo: $', self.saldo, '\n')
    print('\n')

titular = 'FERNANDO JARED ORELLANA NAVARRO'
saldo = 0 #saldo inicial
cuenta = CuentaBancaria(titular, saldo)
cuenta.mostrar_saldo()

dinero = input('Ingrese la cantidad a depositar\n')
dinero = float(dinero)
cuenta.depositar(dinero)
cuenta.mostrar_saldo()

retiro = input('Ingrese la cantidad a retitar\n')
retiro = float(retiro)
cuenta.retirar(retiro)
cuenta.mostrar_saldo()

dinero = input('Ingrese la cantidad a depositar\n')
dinero = float(dinero)
cuenta.depositar(dinero)
cuenta.mostrar_saldo()

retiro = input('Ingrese la cantidad a retitar\n')
retiro = float(retiro)
cuenta.retirar(retiro)
cuenta.mostrar_saldo()