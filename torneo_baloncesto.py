list_puntos = []
list_jugadores = []
list_dorsalJugadores = []
sw = True
import os

def fnt_limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Autor: Yeison Cordoba')
    print('\nTorneo baloncesto\n')
    print('Jugadores: ',list_jugadores)

def fnt_registrarJugadores(numero,nombre):
    if numero == '' or nombre == '':
        enter = input('Debe ingresar todos los datos <ENTER>')
    else:
        list_jugadores.append(nombre)
        list_dorsalJugadores.append(numero)
        list_puntos.append(0)
        enter = input('Jugador almacenado con éxito <ENTER>')

def menu(inic):
    while True:
        print('1. Registrar jugadores')
        print('2. Registrar puntos')
        print('3. Estadisticas')
        print('4. Salir')
        
        opcion = int(input('Opcion: '))
        if opcion == 1:
            nu = input('Ingrese el número del jugador: ')
            nm = input('Ingrese el nombre del jugador: ')
            fnt_registrarJugadores(nu,nm)

        elif opcion == 2:
            jugar()
        elif opcion == 3:
            break
        else:
            print('Opcion no valida')