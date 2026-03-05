from random import randint

def tirada_dados (cantidad):
    dados = []
    for dado in range (cantidad):
        dados.append(randint(1,6))
    return dados


def generala(dados,posiciones):
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
        else:
            print('Opción no válida, escriba s o n.') 
dados = 5
generala(dados,posiciones)
