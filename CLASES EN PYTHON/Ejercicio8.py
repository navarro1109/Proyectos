def contar_vocales(frase):
  vocales = 'aeiouAEIOU'
  contar = 0

  for letra in frase:
    if letra in vocales:
      contar += 1
  
  return contar

frase = input("Ingrese una frase: ")
  
cantidad = contar_vocales(frase)


print("Tiene ", cantidad, " vocales")
