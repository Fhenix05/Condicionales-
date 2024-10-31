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

print('programa que verifica si un número es positivo ')
num = int (input("ingresa un número: "))
# preguntar el número es mayor a 0
if num > 0:
    print('El número es positivo')
else:
    print('El número es negativo')
print('Fin del programa')

print('Programa que verifica si un número es par')
num = int(input('Ingresa un número: '))
if num % 2 == 0:
     print('Es un número par')
else:
    print('Es un número impar')