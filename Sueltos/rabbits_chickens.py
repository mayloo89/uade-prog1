heads = 35
legs = 94

if legs % 2 != 0 :
    print("No hay solución")
else:
    for chickens in range(heads + 1):
        rabbits = heads - 1
    if (chickens * 2) + (rabbits * 4) == legs:
        print("Pollos: ", chickens)
        print("Conejos: ",rabbits)