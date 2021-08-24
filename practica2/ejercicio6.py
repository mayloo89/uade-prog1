# Escribir una funcion que reciba una lista de numeros enteros como parametro y
# la normalice, es decir que todos sus elementos deben sumar 1.0 respetando las 
# proporciones relativas que cada elemento tiene en la lista original.

def normalizar(lista):
    normalizada = []
    auxiliar = []
    cant = 1
    distintos = 0
    tamaño = len(lista)
    lista.sort()

    for x in range(0,tamaño-1):
        if lista[x] == lista[x+1]:
            cant = cant + 1
        else:   
            auxiliar.append(cant)
            distintos = distintos+1
            if x+1 == tamaño-1:
                auxiliar.append(1)
                distintos = distintos+1
    if distintos == 0:
        valor = 1/cant
        while cant > 0:
            normalizada.append(valor)
            cant = cant - 1
        return normalizada

    else:
        for x in auxiliar:
            valor = (1/distintos)/x
            while x > 0:
                normalizada.append(valor)
                x = x - 1
            
            
    return normalizada

def main():
    print("Ingrese los valores de la lista.\nCuando desee salir ingrese 'exit'.\n")

    exit = False
    lista = []

    while exit == False:
        ingreso = input()
        if ingreso.isdigit():
            lista.append(ingreso)
        else:
            if ingreso == 'exit' or ingreso == 'EXIT':
                exit = True
            else:
                print("El valor ingresado es incorrecto.")
            
    if len(lista) == 0:
        print("La lista ingresada esta vacia.")
        return 0
    
    normalizada = normalizar(lista)
    print(normalizada)
    return 0

main()