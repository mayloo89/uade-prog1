n = int(input("Ingrese un numero: "))
divisor = 2

while divisor < n :
    if n % divisor == 0 :
        print(n,"no es un numero primo.")
        break
    divisor += 1
else:
    print(n,"es un numero primo.")