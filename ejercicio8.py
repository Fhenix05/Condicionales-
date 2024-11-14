"""
if expresion_booleana:
    intrucciones
elif expresion_booleana:
    instrucciones
else:
    instrucciones
"""

print("Programa que pida nota, edad y sexo")
nota = float(input("Escrbe la nota: "))
edad = int(input("Escribe tu edad: "))
sexo = input("Escribe tu sexo (F/M): ").upper()

#Comprobar las condiciones
if nota >= 5 and edad >= 18:
    if sexo == "F":
        print("Aceptada")
    else:
        print("Posible")
else:
    print("No aceptada")