from pilacola import *

def main():
    try:
        #Inicializo las dos colas y la finaliliar
        cola1 = inicializarcola()
        cola2 = inicializarcola()
        final = inicializarcola()

        #Cargo valores a las colas
        acolar(cola1,1)
        acolar(cola1,3)
        acolar(cola1,5)

        acolar(cola2,2)
        acolar(cola2,4)
        acolar(cola2,6)
        acolar(cola2,7)
        acolar(cola2,8)

        #Concateno los valores de las dos colas en una
        while not (colavacia(cola1) and colavacia(cola2)):
            if not colavacia(cola1):
                acolar(final,primero(cola1))
                desacolar(cola1)
            if not colavacia(cola2):
                acolar(final,primero(cola2))
                desacolar(cola2)
        
        #Muestro los valores de la cola final
        while not colavacia(final):
            print(primero(final), end=" ")
            desacolar(final)
    except ValueError:
        print("Error de cola vacía.")
    


main()
