# Escribir una funcion que reciba una lista como parametro y devuelva True
# si la lista esta ordenada en forma ascendente o False en caso contrario.

def tieneOrdenAscendente(lista):
    listaOrdenada = sorted(lista)
    for x in range(len(lista)):
        if lista[x] != listaOrdenada[x]:
            return False
    return True

def main():
    print("Ingrese los valores de la lista.\nCuando desee salir ingrese 'exit'.\n")

    exit = False
    lista = []

    while exit == False:
        ingreso = str(input())
        if ingreso == 'exit' or ingreso == 'EXIT':
            exit = True
        else:
            lista.append(ingreso)
            

    if len(lista) == 0:
        print("La lista ingresada esta vacia.")
        return 0

    if tieneOrdenAscendente(lista):
        print("La lista ingresada esta ordenada de forma ascendente.")
    else:
        print("La lista ingresada no esta ordenada de forma ascendente.")

    return 0

main()