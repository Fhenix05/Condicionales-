"""

"""

print("Programa que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.")
alum = int(input("Escribe la cantidad de alumnos: "))

if alum >=100:
    pay = alum * 65
    print("El costo de la renta del autobus es: €",pay)
elif alum >=50 and alum <99:
    pay = alum * 70
    print("El costo de la renta del autobus es: €",pay)
elif alum >=30 and alum <49:
    pay = alum * 95
    print("El costo de la renta del autobus es: €",pay)
else:
    pay = 4000 / alum
    print("El costo por cada alumno es de: €",pay)