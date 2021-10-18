# Desarrolle un programa para eliminar todos los comentarios de un programa 
# escrito en Python. Tener en cuenta que los comentarios comienzan con # 
# (siempre que no este entre comillas) y que
# tambien se consideran comentarios las cadenas de documentacion (dosctrings).


def extraeComentarios():
    rutaArchivo = "/home/seba/Documentos/UADE/Programacion I/git/uade-prog1/practica6/archivos/prueba.py"

    try:
        archEntrada = open(rutaArchivo,"rt")
        archSalida = open("/home/seba/Documentos/UADE/Programacion I/git/uade-prog1/practica6/archivos/salida.py", "wt")
        linea = archEntrada.readline()


        while linea:
            pos = 0
            while linea[pos] == " " or linea[pos:pos+1] == "\n":
                pos = pos + 1
            char = linea[pos]
            char2 = linea[pos:pos+3]
            if linea[pos] != "#":
                if linea[pos:pos+3] == "\"\"\"":
                    aux = linea.rfind("\"\"\"")
                    if aux == pos:
                        fin = False
                        while not fin:
                            linea = archEntrada.readline()
                            aux = linea.rfind("\"\"\"")
                            if aux > 0 and aux != pos:
                                fin = True
                else: 
                    archSalida.write(linea)
                
            linea = archEntrada.readline()


       
    except OSError as message:
        print("No se pudo abrir el archivo:", message)
    
    finally:
        try:
            archEntrada.close()
        except NameError:
            pass


extraeComentarios()