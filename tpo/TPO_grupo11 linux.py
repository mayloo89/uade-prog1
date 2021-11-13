import os

def cargarNivel(ruta):
    """Lee el archivo con el juego y devuelve una matriz con sus valores"""

    try:
        matriz = []
        archEntrada = open(ruta,"rt")
        linea = archEntrada.readline()
        linea = linea.rstrip('\n')
        linea = linea.split(",")
        tam = len(linea)

        while linea and tam > 0:
            matriz.append(linea)

            linea = archEntrada.readline()
            linea = linea.rstrip('\n')
            linea = linea.split(",")
            tam = tam - 1
        
        return matriz

    except OSError as message:
        print("No se pudo abrir el archivo:", message)
    finally:
        try:
            archEntrada.close()
        except NameError:
            pass

    return 0

def muestraTablero(matriz):
    
    #Encabezado
    tam = len(matriz)
    linea = ""
    while tam > 0:
        linea = " " + str(tam) + "  " + linea
        tam = tam - 1
    linea = "   " + linea
    print(linea)
    print("  |" + "---|" * len(matriz))

    y = 1
    for fila in matriz:
        linea = " " + str(y) + "|"
        for valor in fila:
            linea = linea + " " + valor + " |"

        print(linea)
        print("  " + "|---" * len(matriz) + "|")
        y = y + 1

def inicializaTablero(tam):
    matriz = []
    for i in range(tam):
        matriz.append([])
        for j in range(tam):
            matriz[i].append("·")
    return matriz

def mina(base, jugador, puntaje, mov, fila, columna):
    #Borra la termianl
    os.system('cls||clear')

    print("BOOM! Explotaste una mina =(")
    print("\n¡Fin del juego!\n\n")
    
    jugador[fila][columna] = base[fila][columna]
    muestraTablero(jugador)

    print("\nTu puntaje total:" + str(puntaje))
    print("Cant. de movimientos: " + str(mov) + "\n")
    
    
    
    

def repetido():
    print("Casillero ya seleccionado, intenta con otro.")
    input()
   

def ok(base, jugador, fila, columna):
    jugador[fila][columna] = base[fila][columna]

dic = {
	"M": mina,
	"R": repetido,
	"OK": ok,
}

def checkTablero(base, jugador, puntaje, mov, fila, columna):
    if base[fila][columna] == "M":
         dic.get("M")(base, jugador, puntaje, mov, fila, columna)
         return False, 0, 0
    elif jugador[fila][columna] != "·":
        dic.get("R")()
        return True, 0, 0
    dic.get("OK")(base, jugador, fila, columna)
    return True, int(jugador[fila][columna]), 1



def main():
    #Carga el juego desde archivo
    tableroBase = cargarNivel("/home/seba/Documentos/UADE/Programacion I/git/uade-prog1/tpo/nivel_2.txt")
    
    tam = len(tableroBase)
    puntaje = 0
    mov = 0

    #Bienvenida
    os.system('cls||clear')
    print("Bienvenido al buscaminas.\n")
    print("Veamos cuantos puntos logras antes de dar con una de las minas!\n\n")
    print("¿Comenzamos?")
    input("Presione una tecla para continuar")

    #Inicializa matriz del jugador
    tableroJugador = inicializaTablero(tam)

    #Ciclo del juego
    sigueJugando = True
    while sigueJugando:
        #Borra la termianl
        os.system('cls||clear')

        #Muestro el tablero
        muestraTablero(tableroJugador)

        #Ingreso de valores
        ingreso = input("\nIngrese la coordenada en formato fila columna (Ej: 1 3) = ").split()

        #Verifica los valores ingresados
        try: 
            val = list(map(int, ingreso))
            if val[0] > tam or val[0] < 1 or val[1] > tam or val[1] < 1:
                print("Error en el ingreso! Intente nuevamente.")
                input("Presione una tecla para continuar")
                continue
        except ValueError:
            print("Error en el ingreso! Intente nuevamente.")
            input("Presione una tecla para continuar")
            continue        
        
        # Obtengo las coordenadas ingresadas
        fila = val[0]-1
        columna = val[1]-1

        #Chequeo el valor en el tablero
        sigueJugando, puntos, movimientos = checkTablero(tableroBase, tableroJugador, puntaje, mov, fila, columna)
        puntaje = puntaje + puntos
        mov = mov + movimientos

main()