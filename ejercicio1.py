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

  if expresion:
    instrucciones
  elif expresion:
      instrucciones
  else:
      intrucciones
"""

#Solicita al usuario que ingrese dos números
print ("Programa que pida dos números e indique Cuál es el mayor o si los dos son iguales")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

#Comparamos números y mostramos el resultado
if num1 > num2:
    print("El primer número es mayor que el segundo.")
elif num2 > num1:
    print("El segundo número es mayor que el primero.")
else:
    print("Son iguales") 