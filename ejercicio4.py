"""
Condicionales if:
    Evaluan expresiones booleanas

Estructuras:
  if expresion:
    instrucciones

  if expresion:
    instrucciones
  else:
    instrucciones
"""

print ("Programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario")
num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

if num2 != 0:
     resultado = num1/num2
     print("El resultado es: ", resultado)
else:
     print("Error")     