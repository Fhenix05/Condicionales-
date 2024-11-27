"""

"""
opciones =  ["Piedra", "Papel", "Tijeras"]
print("Bienvenidos a piedra papel o tijeras")
jugador1 = input("Jugador uno escoge piera, papel o tijeras: ")
jugador2 = input("Jugador dos escoge piera, papel o tijeras: ")

if jugador1 not in opciones or jugador2 not in opciones:
    print("Opción incorrecta. Ambos jugadores deben elegir entre piedra, papel o tijeras")

if jugador1 == jugador2:
    print("Empate")

if (jugador1 == "Piedra" and jugador2 == "Tijeras") or \
    (jugador1 == "Papel" and jugador2 == "Piedra") or \
     (jugador1 == "Tijeras" and jugador2 == "Papel"):
     print("Jugador uno gana")
else:
    print("Jugador dos")