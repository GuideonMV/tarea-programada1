def estarVacio(pArchivo):
    for linea in pArchivo:
        pArchivo.seek(0)
        return False
    return True
def cargarTokensAux(tokens):
    while True:
        nombreArchivo = input("Ingrese el nombre del archivo: ")
        try:
            archivo = open(nombreArchivo, "r")
            if estarVacio(archivo):
                print("El archivo ingresado está vacío")
                archivo.close()
            else:
                break
        except:
            print("El archivo ingresado no existe")
    while True:
        separador = input("Ingrese el separador utilizado: ")
        try:
            for linea in archivo:
                partes = linea.split(separador)
                palabraReservada = partes[0].strip()
                reemplazo = partes[1].strip()
                tokens.append((palabraReservada, reemplazo))
            archivo.close()
            return cargarTokens()
        except:
            print("El separador ingresado no es correcto")
def cargarTokens():
        print("====================================")
        return "¡Tokens agregados correctamente!"
def mostrarTokens(listaTokens):
    if len(listaTokens) == 0:
        print("No hay tokens cargados")
        return
    print("\n===========TOKENS CARGADOS===========")
    for tupla in listaTokens:
        print(tupla[0], "->", tupla[1])
   