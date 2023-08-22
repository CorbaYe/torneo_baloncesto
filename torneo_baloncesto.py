list_puntos = []
list_jugadores = []
list_dorsalJugadores = []
sw = True
import os

def fnt_limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Autor: Yeison Cordoba')
    print('Torneo baloncesto')
    print('Jugadores: ',list_jugadores, '\n')

def fnt_registrarJugadores(numero,nombre):
    if numero == '' or nombre == '':
        enter = input('Debe ingresar todos los datos <ENTER>...')
    else:
        list_jugadores.append(nombre)
        list_dorsalJugadores.append(numero)
        list_puntos.append(0)
        enter = input('Jugador almacenado con éxito <ENTER>...')

def fnt_estadistica():
        fnt_limpiar()
        print('<<<< ESTADISTICA >>>>')
        print('Jugador     - Número     - Puntaje')
        for i in range(0,len(list_jugadores)):
            print(list_jugadores[i],'       ',list_dorsalJugadores[i],'             ',list_puntos[i])
        enter = input('Fin de estadistica <ENTER>...')

def fnt_menu(inic):
    while (inic == True):
        fnt_limpiar()
        print('1. Registrar jugadores')
        print('2. Registrar puntos')
        print('3. Estadisticas')
        print('4. Salir')

        opcion = int(input('Opcion: '))
        if opcion == 1:
            nm = input('Ingrese el nombre del jugador: ')
            nu = input('Ingrese el número del jugador: ')
            fnt_registrarJugadores(nu,nm)

        elif opcion == 2:
            jugar()

        elif opcion == 3:
            fnt_estadistica()    

        elif opcion == 4:
            inic = False

        else:
            enter = input('Opcion no valida <ENTER>...')

fnt_menu(True)