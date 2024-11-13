"""
 if expresion_booleana:
    instrucciones
elif expresion_booleana:
    instrucciones
else:
    instrucciones
"""

print("Programa que calcule la potencia")
base = int(input("Introduce la base: "))
exp = int(input("Escribe el exponente: "))

if exp > 0:
    res = base ** exp
    print(f"El resultado es: {res}")
elif exp ==0:
    resp = 1
    print(f"El resultado es: {resp}")
else:
    resultado =1 / (base ** abs(exp))
    print(f"El resultado es: {resultado}")