def cargarTokens(tokens):
    nombreArchivo = input("Ingrese el nonmbre del archivo: ")
    separador = input("Ingrese el separador utilizado: ")
    archivo = open(nombreArchivo, "r")
    for linea in archivo:
        partes = linea.split(separador)
        palabraReservada= partes[0].strip()
        reemplazo = partes[1].strip()
        tokens.append((palabraReservada, reemplazo))
    archivo.close()
    return tokens