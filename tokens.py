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
    print("====================================")
    return "¡Tokens agregados correctamente!"

def mostrarTokens(listaTokens):
    if len(listaTokens) == 0:
        print("No hay tokens cargados")
        return
    print("\n===========TOKENS CARGADOS===========")
    for tupla in listaTokens:
        print(tupla[0], "->", tupla[1])
   