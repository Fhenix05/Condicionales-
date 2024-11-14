"""
if expresion:
   instrucciones
if expresion:
   instrucciones
else:
   instrucciones

if expresion:
   instrucciones
if expresion:
   instrucciones
else:
   instrucciones

if expresion:
   instrucciones
if expresion:
   instrucciones
else:
   instrucciones
"""

print("Programa que pida tres números y los ordene de mayor a menor")
num = (input("Escribe un número: "))
numa = (input("Escribe un número: "))
numb = (input("Escribe un número: "))

if num > numa and num > numb:
    print(num)
    if numa > numb:
        print(numa)
        print(numb)
    else:
        print(numb)
        print(numa)
if numa > num and numa > numb:
    print(numa)
    if num > numb:
        print(num)
        print(numb)
    else:
        print(numb)
        print(num)
if numb > num and numb > numa:
    print(numb)
    if num > numa:
        print(num)
        print(numa)
    else:
        print(numa)
        print(num)