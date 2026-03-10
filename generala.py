from random import randint

def tirada_dados (cantidad):
    dados = []
    for dado in range (cantidad):
        dados.append(randint(1,6))
    return dados

def jugar_turno(nombre_jugador):
    print(f"\n--- TURNO DE: {nombre_jugador} ---") ###
    dados_actuales = tirada_dados (5)
    tiradas = 1
    print('Tus dados actuales son: ', dados_actuales)
    while tiradas < 3:
        continuar = input('Desea continuar? Si lo desea: escriba s, de lo contrario, escriba n: ')
        if continuar == 'n':
            break
        if continuar == 's':
            cambiar = input('Que posiciones desea cambiar (0 al 4): ')
            posiciones_a_cambiar = [int(p) for p in cambiar.split()] # Reemplazamos SOLO los dados en esas posiciones
            for i in posiciones_a_cambiar:
                if 0 <= i <= 4: # Validamos que la posición sea correcta
                    dados_actuales[i] = randint(1, 6)
            tiradas += 1
            print('Tus nuevos dados son: ', dados_actuales)
        else:
            print('Opción no válida, escriba s o n.')
    print('Fin del turno. Tus dados finales son: ', dados_actuales)
    return dados_actuales

def generala():
    print('Bienvenido al juego de la generala!!!')
    jugar = ''
    while jugar != '1' :
        jugar = input('Presione 1 para jugar:')
    for ronda in range(1,12):
        print("\n=== RONDA", ronda, "===") ###
        dados_j1 = jugar_turno ('Jugador 1')
        dados_j2 = jugar_turno ('Jugador 2')

generala()
