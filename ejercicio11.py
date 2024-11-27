"""

"""

turno = input ("Ingrese el turno del día (mañana o tarde): ")
duracion = float(input("Ingrese la duración de la llamada en minutos: "))
dia_semana =input("Ingrese el día de la semana (lunes, martes, ... domingo): ")

pre_prim_5_min = 1 # en euros
pre_sig_3_min = 0.80 # en euros
pre_sig_2_min = 0.70 # en euros
pre_par_10_min = 0.50 # en euros

if duracion <= 5:
    costo = duracion * (pre_prim_5_min / 5)
else:
    if duracion <= 8:
        costo = pre_prim_5_min + (duracion - 5) * (pre_sig_3_min / 3)
    else:
        if duracion <= 10:
            costo = pre_prim_5_min + pre_sig_3_min + (duracion - 8) * (pre_sig_2_min / 2)
        else:
            costo = pre_prim_5_min + pre_sig_3_min + pre_sig_2_min + (duracion - 10) * (pre_par_10_min / 5)

if dia_semana == "domingo":
    impuesto = 0.03 # 3 % en domingo
elif turno == "mañana":
    impuesto = 0.15 # 15 % en turno de mañana (lunes a sábado)
else:
    impuesto = 0.10 # 10 % en turno de tarde (lunes a sábado)

pay_to = costo + (costo * impuesto)

print("El precio es de:€ ", pay_to)