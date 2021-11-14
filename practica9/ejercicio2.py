from pilacola import *

def main():
    #Inicializo pila
    pila = inicializarpila()
    
    #El usuario carga elementos en pila
    while pilavacia(pila):
        elemento = int(input("Ingrese un elemento o -1 para finalizar: "))

        while elemento != -1:
            apilar(pila, elemento)
            elemento = int(input("Ingrese un elemento o -1 para finalizar: "))

    #Invierte el orden de pila
    aux = inicializarpila()
    while not pilavacia(pila):
        apilar(aux, tope(pila))
        desapilar(pila)

    #Imprime pila invertida
    while not pilavacia(aux):
        print(tope(aux), end=" ")
        desapilar(aux)

main()
