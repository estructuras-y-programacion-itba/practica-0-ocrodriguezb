from random import randint

def tirada_dados (cantidad):
    dados = []
    for dado in range (cantidad):
        dados.append(randint(1,6))
    return dados


def generala(dados):
    print('Bienvenido al juego de la generala!!!')
    tiradas = 0
    cont_jugador = 1
    seguir = True
    jugar = ''
    while jugar != '1' :
        jugar = input('Presione 1 para jugar:')
    dados_actuales = tirada_dados (5)
    tiradas += 1
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
dados = 5
generala(dados)

## me falta poder cambiar mas de una posicion por turno ; armarlo para dos jugadores ; toda la parte de puntos y ganadores