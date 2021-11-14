def inicializarpila():
    pila = []
    return pila

def apilar(pila, dato):
    pila.append(dato)

def desapilar(pila):
    if len(pila) > 0:
        pila.pop()
    else:
        raise ValueError("Pila vacía")

def tope(pila):
    if len(pila) > 0:
        return pila[-1]
    else:
        raise ValueError("Pila vacía")

def pilavacia(pila):
    return len(pila) == 0

def inicializarcola():
    cola = []
    return cola

def acolar(cola, dato):
    cola.append(dato)

def desacolar(cola):
    if len(cola) > 0:
        cola.pop(0)
    else:
        raise ValueError("Cola vacía")

def primero(cola):
    if len(cola) > 0:
        return cola[0]
    else:
        raise ValueError("Cola vacía")

def colavacia(cola):
    return len(cola) == 0