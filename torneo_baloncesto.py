listPuntos = []
listJugadores = []
listDorsalJugadores = []
sw = True
import os

def fntLimpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Autor: Yeison Cordoba')
    print('Torneo baloncesto')
    print('Jugadores: ',listJugadores, '\n')

def fntRegistrarJugadores(numero,nombre):
    if numero == '' or nombre == '':
        enter = input('Debe ingresar todos los datos <ENTER>...')
    else:
        listJugadores.append(nombre)
        listDorsalJugadores.append(numero)
        listPuntos.append(0)
        enter = input('Jugador almacenado con éxito <ENTER>...')

def fntRegistrarPuntos(nombre,numero,puntos):
    if nombre != '' and numero != '':
        for i in range(0,len(listJugadores)):
            if listJugadores[i] == nombre and listDorsalJugadores[i] == numero:
                listPuntos[i] += puntos
                enter = input('Puntos almacenados con éxito <ENTER>...')
                break
        else:
            enter = input('Jugador no registrado <ENTER>...')
    else:
        enter = input('Debe ingresar todos los datos <ENTER>...')

def fntEstadistica():
        fntLimpiar()
        print('<<<< ESTADISTICA >>>>')
        print('Jugador     - Número     - Puntaje')
        for i in range(0,len(listJugadores)):
            print(listJugadores[i],'       ',listDorsalJugadores[i],'             ',listPuntos[i])
        enter = input('Fin de estadistica <ENTER>...')

def fntMenu(inic):
    while (inic == True):
        fntLimpiar()
        print('1. Registrar jugadores')
        print('2. Registrar puntos')
        print('3. Estadisticas')
        print('4. Salir')

        opcion = int(input('Opcion: '))
        if opcion == 1:
            nm = input('Ingrese el nombre del jugador: ')
            nu = input('Ingrese el número del jugador: ')
            fntRegistrarJugadores(nu,nm)

        elif opcion == 2:
            nm = input('Ingrese el nombre del jugador: ')
            nu = input('Ingrese el número del jugador: ')
            pt = input('Ingrese los puntos: ')
            if pt == '':
                enter = input('Debe ingresar todos los datos <ENTER>...')
            else:
                pt = int(pt.strip())
                fntRegistrarPuntos(nm,nu,pt)

        elif opcion == 3:
            fntEstadistica()    

        elif opcion == 4:
            inic = False

        else:
            enter = input('Opcion no valida <ENTER>...')

fntMenu(True)