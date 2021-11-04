# Desarrolle un programa para eliminar todos los comentarios de un programa 
# escrito en Python. Tener en cuenta que los comentarios comienzan con # 
# (siempre que no este entre comillas) y que
# tambien se consideran comentarios las cadenas de documentacion (dosctrings).

# Se considera que en donde haya un docstring no va a haber codigo por fuera de la misma.


def extraeComentarios():
    rutaArchivo = "/home/seba/Documentos/UADE/Programacion I/git/uade-prog1/practica6/archivos/prueba.py"
    docstringSimple = "\'\'\'"
    docstringDoble = "\"\"\""

    try:
        archEntrada = open(rutaArchivo,"rt")
        archSalida = open("/home/seba/Documentos/UADE/Programacion I/git/uade-prog1/practica6/archivos/salida.py", "wt")
        linea = archEntrada.readline()


        while linea:
            # Busco comentarios y docstring en la linea
            posComentario = linea.find("#")
            posSimples = linea.find(docstringSimple)
            posDobles = linea.find(docstringDoble)

            if posComentario >= 0:
                #Hay comentario.
                if posComentario > 0:
                    hayTexto = False
                    auxLinea = linea[0:posComentario-1]
                    for char in auxLinea:
                        if char != " ":
                            hayTexto = True
                    
                    if hayTexto:
                        #Escribo lo que haya en la linea antes del comentario.
                        auxLinea = auxLinea + "\n"
                        archSalida.write(auxLinea)
            else:
                if (posSimples >= 0 or posDobles >= 0):
                    #Hay dosctring
                    if (posSimples >= 0 and posDobles == -1):
                        #Es de comillas simples
                        comillas = docstringSimple
                        pos = posSimples
                    else:
                        if (posDobles >= 0 and posSimples == -1):
                            #Es de comillas dobles
                            comillas = docstringDoble
                            pos = posDobles
                        else:
                            # Hay comillas simples y dobles. Determinar cual inicia el docstring.
                            if (posSimples < posDobles):
                                comillas = docstringSimple
                                pos = posSimples
                            else: 
                                comillas = docstringDoble
                                pos = posDobles

                    #Busco si el docstring termina en la misma linea o es multilinea.
                    aux = linea.rfind(comillas)
                    if aux == pos:
                        fin = False
                        while not fin:
                            linea = archEntrada.readline()
                            aux = linea.rfind(comillas)
                            if aux > 0:
                                #Encontre el fin del docstring. Salgo del loop.
                                fin = True
                else:
                    #No hay comentario ni docstring. Escribo en el nuevo archivo.
                    archSalida.write(linea)
            #Leo la siguiente linea del archivo.
            linea = archEntrada.readline()

    except OSError as message:
        print("No se pudo abrir el archivo:", message)
    
    finally:
        try:
            archEntrada.close()
        except NameError:
            pass


extraeComentarios()