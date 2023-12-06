from random import randint

while True:
    
    usuario = 0
    pc = 0
    
    jugadas = """
    Jugadas posibles:
    1. Piedra
    2. Papel
    3. Tijera
    """
    print(jugadas)
    usuario = int(input("Ingrese su jugada: "))
    
    if usuario == 1:
        j_usuario = "Piedra"
    elif usuario == 2:
        j_usuario = "Papel"
    elif usuario == 3:
        j_usuario = "Tijera"
    
    pc = randint(1,3)
    
    if pc == 1:
        j_pc = "Piedra"
    elif pc == 2:
        j_pc = "Papel"
    elif pc == 3:
        j_pc = "Tijera"

    print(f"Su jugada fue {j_usuario}, y la PC jugó {j_pc}")
    
    if usuario == 1 and pc == 2:
        print("La PC ganó")
    elif usuario == 2 and pc == 3:
        print("La PC ganó")
    elif usuario == 3 and pc == 1:
        print("La PC ganó")
        
    elif pc == 2 and usuario == 3:
        print("Usted ganó!")
    elif pc == 3 and usuario == 1:
        print("Usted ganó!")
    elif pc == 1 and usuario == 2:
        print("Usted ganó!")        
    elif pc == usuario:
        print("Empate!")
        
    entrada = input("¿Jugar de nuevo? (y/n)")
    if entrada == "n":
        break

