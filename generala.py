from random import randint

def tirada_dados (cantidad):
    dados = []
    for dado in range (cantidad):
        dados.append(randint(1,6))
    return dados

def calcular_puntos(dados):
    dados_ordenados = sorted(dados)
    if dados_ordenados == [1,2,3,4,5] or dados_ordenados == [2,3,4,5,6] or dados_ordenados == [1,3,4,5,6]:
        return 'E' , 20
    conteos= [dados.count(i) for i in set(dados)]
    if 5 in conteos:
        return 'G' , 50
    if 4 in conteos:
        return 'P' , 40
    if 3 in conteos and 2 in conteos:
        return 'F' , 30
    return None , 0

def calcular_puntuacion(dados,tirada,categoria):
    if categoria in ['1','2','3','4','5','6']:
        num = int(categoria)
        return dados.count(num) * num
    dados_ordenados = sorted(dados)
    conteos= [dados.count(i) for i in set(dados)]
    es_primera = (tirada == 1)
    if categoria == 'E':
        if dados_ordenados in [[1,2,3,4,5],[2,3,4,5,6],[1,3,4,5,6]]:
            if es_primera:
                return 25
            else:
                return 20
        return 0
    if categoria == 'F':
        if 3 in conteos and 2 in conteos:
            if es_primera:
                return 35
            else:
                return 30
        return 0
    if categoria == 'P':
        if 4 in conteos:
            if es_primera:
                return 45
            else:
                return 40
        return 0
    if categoria == 'G':
        if 5 in conteos:
            if es_primera:
                print('GENERALAAAAA!!! VICTORIA AUTOMATICA')
                return 80
            return 50
        return 0
    return 0

def jugar_turno(nombre_jugador,planilla_actual):
    print('\n--- TURNO DE: ',nombre_jugador,' ---')
    dados_actuales = tirada_dados (5)
    tiradas = 1
    print('Tus dados actuales son: ', dados_actuales)
    while tiradas < 3:
        continuar = input('Desea continuar? Si lo desea: escriba s, de lo contrario, escriba n: ')
        if continuar == 'n':
            break
        if continuar == 's':
            cambiar = input('Que posiciones desea cambiar (0 al 4, separado con espacios): ') ### revisar esto!!!
            posiciones_a_cambiar = [int(p) for p in cambiar.split()] # Reemplazamos SOLO los dados en esas posiciones
            for i in posiciones_a_cambiar:
                if 0 <= i <= 4: # Validamos que la posición sea correcta
                    dados_actuales[i] = randint(1, 6)
            tiradas += 1
            print('Tus nuevos dados son: ', dados_actuales)
        else:
            print('Opción no válida, escriba s o n.')
    print('Fin del turno. Tus dados finales son: ', dados_actuales)

    libres = []
    for categoria, puntaje in planilla_actual.items():
        if puntaje is None: #Si el puntaje es None, significa que esa jugada no se usó
            libres.append(categoria)
    print('Categorías disponibles:', libres)
    
    eleccion = ''
    while eleccion not in libres:
        eleccion = input('¿En qué categoría querés anotar los puntos?: ').upper()
        if eleccion not in libres:
            print('Categoría no válida o ya ocupada. Elegí otra.') 
    puntos = calcular_puntuacion(dados_actuales, tiradas, eleccion) # Calculamos los puntos
    planilla_actual[eleccion] = puntos # Guardamos en la planilla
    print('Anotaste ', puntos, 'puntos en ', eleccion)
    es_generala_real = (eleccion == 'G' and puntos == 80)
    return es_generala_real

def generala():
    print('Bienvenido al juego de la generala!!!')
    jugar = ''
    while jugar != '1' :
        jugar = input('Presione 1 para jugar:')
    categorias = ['1','2','3','4','5','6','E','F','P','G']
    planilla_j1 = {cat:None for cat in categorias}
    planilla_j2 = {cat:None for cat in categorias}
    for ronda in range(1, 11):
        print('\n=== RONDA', ronda, '===')

        victoria_j1 = jugar_turno('Jugador 1', planilla_j1) 
        guardar_csv(planilla_j1,planilla_j2)
        if victoria_j1: 
            break
        victoria_j2 = jugar_turno('Jugador 2', planilla_j2)
        guardar_csv(planilla_j1,planilla_j2)
        if victoria_j2: 
            break

    total_j1 = sum(v for v in planilla_j1.values() if v is not None)
    total_j2 = sum(v for v in planilla_j2.values() if v is not None)
    
    print('\n--- PUNTAJE FINAL ---')
    print('Jugador 1: ',total_j1)
    print('Jugador 2: ',total_j2)
    
    if total_j1 > total_j2:
        print('¡Ganador: Jugador 1!')
    elif total_j2 > total_j1:
        print('¡Ganador: Jugador 2!')
    else:
        print('¡Empate!')      

def guardar_csv(planilla_j1,planilla_j2):
    try:
        with open('jugadas.csv','w') as archivo:
            archivo.write('jugada,j1,j2\n')

            for cat in planilla_j1.keys():
                if planilla_j1[cat] is not None:
                    v1 = planilla_j1[cat]
                else:
                    v1 = 0
                if planilla_j2[cat] is not None:
                    v2 = planilla_j2[cat]
                else:
                    v2 = 0
                linea = str(cat) + ',' + str(v1) + ',' + str(v2) + '\n'
                archivo.write(linea)
        print('Planilla guardada en jugadas.csv')
    except:
        print('Error al guardar el archivo')

generala()

#juego terminado