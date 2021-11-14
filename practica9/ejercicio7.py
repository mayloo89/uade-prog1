from pilacola import *

def main():
    cola = inicializarcola()
    aux = inicializarcola()
    colados = inicializarcola()

    acolar(cola,("A001",30333111))
    acolar(cola,("A002",30444222))
    acolar(cola,("none",30555333))
    acolar(cola,("B001",30666444))
    acolar(cola,("none",30777555))
    acolar(cola,("B002",30888666))

    print("Cola original:")
    while not colavacia(cola):
        primer = primero(cola)

        #Imprime cola original
        print(primer, end="\n")

        #Evalua si es un colado
        if primer[0] != "none":
            acolar(aux, primer)
        else:
            acolar(colados, primer)
        desacolar(cola)

    print("\nDNI de colados:")
    while not colavacia(colados):
        colado = primero(colados)
        print(colado[1], end="\n")
        desacolar(colados)
    
    print("\nCola sin colados:")
    while not colavacia(aux):
        print(primero(aux), end="\n")
        desacolar(aux)


main()