"""
if expresion_booleana:
    instrucciones
else:
    instrucciones
"""

print("Progra que lea una cadena por teclado yy compruebe si es una letra mayúscula")
letra = input("Escribe una letra: ")
if len(letra) == 1:
    if letra == letra.upper():
        print('Letra Mayúscula!')
    else:
        print('Letra Minúscula')
else:
    print('Debes escribir solo una letra')