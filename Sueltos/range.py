#Imprimir los valores impares entre 0 y N

n = int(input("Ingrese un numero: "))
for i in range(1, n+1, 2):
    print(i, end=" ")
print()