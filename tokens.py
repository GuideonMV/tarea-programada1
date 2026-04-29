def estarVacio(pArchivo):
    for linea in pArchivo:
        pArchivo.seek(0)
        return False
    return True

def cargarTokensAux(tokens):
    while True:
        nombreArchivo = input("Ingrese el nombre del archivo: ")
        try:
            with open(nombreArchivo, "r", encoding="utf-8") as archivo:
                if estarVacio(archivo):
                    print("El archivo ingresado está vacío")   
                else:
                    while True:
                        separador = input("Ingrese el separador utilizado: ")
                        try:
                            cargarTokens(tokens,archivo,separador)
                            print("====================================")
                            return "¡Tokens agregados correctamente!"
                        except:
                            print("El separador ingresado no es correcto")
        except:
            print("El archivo ingresado no existe")

def cargarTokens(tokens,archivo,separador):
    for linea in archivo:
        partes = linea.split(separador)
        palabraReservada = partes[0].strip()
        reemplazo = partes[1].strip()
        tokens.append((palabraReservada, reemplazo))
    return " "

def mostrarTokens(pListaTokens):
    if not mostrarTokensAux(pListaTokens):
        print("===========TOKENS CARGADOS===========")
        for tupla in pListaTokens:
            print(tupla[0], "->", tupla[1])
        return

def mostrarTokensAux(pListaTokens):
    if len(pListaTokens) == 0:
        print("El archivo ingreso se encuentra vacío")
        return True
    return False
    
def agregarModif(pListaTokens):
    textoTokens= input("Ingrese texto a procesar: ")
    separador = input("Ingrese el sepador utilizado en el texto: ")
    print("====================================")
    tokens = textoTokens.split()
    for elemento in tokens:
        elemento = elemento.strip()
        partes = elemento.split(separador)
        palabraReservada = partes[0]
        traduccion = partes[1]
        if existeToken(pListaTokens, palabraReservada):
            print(f"¡El token '{palabraReservada + " " + separador + " " + traduccion}' se encontró en la base de datos!\nSe procederá a modificarlo")
            print("====================================")
            print(modificarToken(pListaTokens, palabraReservada))
            print("====================================")
        else:
            print(f"No se encontró el token '{palabraReservada + " " + separador + " " + traduccion}' en la base de datos\nSe procederá a agregarlo")
            print("====================================")
            print(agregarToken(pListaTokens, palabraReservada, traduccion))
    print("====================================")
    return "Proceso finalizado :)"

def existeToken(pListaTokens, pToken):
    for tupla in pListaTokens:
        if pToken == tupla[0]:
            return True
    return False

def modificarToken(pListaTokens, pPalabraReservada):
        for i in range(len(pListaTokens)):
            tupla = pListaTokens[i]
            palabraReservada = tupla[0]
            if palabraReservada == pPalabraReservada:
                nuevoReemplazo = input("Ingrese el nuevo reemplazo: ")
                pListaTokens[i] = (pPalabraReservada, nuevoReemplazo)
                print("====================================")
        return "¡El token ha sido modificado correctamente!"
               
def agregarToken(pListaTokens, pPalabraReservada, pTraduccion):
    nuevoToken = [pPalabraReservada, pTraduccion]
    pListaTokens.append(nuevoToken)
    return "¡El token se agregó correctamente!"

def guardarArchivo(pListaTokens):
    nombreArchNuev = input("Ingrese el nombre del archivo a crear: ")
    separador = input("Ingrese el separador que desea usar: ")

    with open(nombreArchNuev, "w", encoding="utf-8") as archivo:
        for palabra, token in pListaTokens:
            linea = palabra + " " + separador + " " + token + "\n"
            archivo.write(linea)
    print("====================================")
    return "¡Archivo guardado correctamente!"

def traducirTokens(pListaTokens):
    nombre = input("Ingrese el nombre del archivo a traducir: ")
    nombreNuev = input("Ingrese el nombre del nuevo archivo: ")
    resultado = []
    with open(nombre, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            espacios = len(linea) - len(linea.lstrip())
            contenido = linea.strip()
            palabras = contenido.split()
            nueva = []
            for palabra in palabras:
                for original, traduccion in pListaTokens:
                    if "print" in palabra:
                        palabra = "pinte"
                    if palabra == original:
                        palabra = traduccion
                        break
                nueva.append(palabra)
            nuevaLinea = " " * espacios + " ".join(nueva)
            resultado.append(nuevaLinea)
    with open(nombreNuev, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(resultado))
    return "¡Se ha realizado correctamente la traducción!"

