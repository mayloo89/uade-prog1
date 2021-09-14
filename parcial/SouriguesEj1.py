import random

def crearMatriz(m,n):
    """Crea una matriz de tamaño m x n con valores aleatorios del 0 al 25, sin repetir numeros porcada columna."""

    matriz = []
    for x in range(m):
        matriz.append([])
        for y in range(n):
            numero = random.randint(0, 25)
            if x != 0:
                z = 0
                while z < x:
                    if matriz[z][y] == numero:
                        numero = random.randint(0, 25)
                        z = 0
                    else:
                        z = z + 1
                
            matriz[x].append(numero)

    return matriz

def imprimirMatriz(matriz,m,n):
    """Imprime en pantalla la matriz de tamaño m x n."""

    for i in range(m):
        for x in range(n):
            print(f'{matriz[i][x]:02}',end="  ")
        if matriz[i][x] == matriz[i][n-1]:
            print()


#Programa principal
def main():
    """Programa principal que solicita el tamaño de la matriz e invoca su creacion e impresion."""
    
    print("Ingrese el tamaño de la matriz a crear")
    m= int(input("Cant. de columnas: "))
    n= int(input("Cant. de filas: "))
    print()

    imprimirMatriz(crearMatriz(m,n),m,n)

    return 0

#Invocacion del programa principal
main()
