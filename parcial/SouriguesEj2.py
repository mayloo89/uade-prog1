

def darFormatoMonetario(numero):
    """Da formato de moneda local al valor ingresado como numero."""
    
    #Se redondean los decimales a dos digitos
    numero = round(float(numero), 2)
    
    #Se reemplaza el separador de decimales "." a ","
    numero = str(numero).replace(".",",")

    #Se busca la posicion del separador de decimales y se agregan los separadores de millar
    pos = str(numero).find(",")
    while pos > 3:
        numero = str(numero[:pos-3]) + "." + str(numero[pos-3:])
        pos = pos - 3

    return numero

#Programa principal
def main():
    """Programa principal que solicita el numero a ser formateado."""

    num = input("Ingrese el numero a formatear: ")
    num = darFormatoMonetario(num)
    print(f"El numero ingresado con formato es: ${num}")
    
    return 0

#Ejecucion del programa principal
main()