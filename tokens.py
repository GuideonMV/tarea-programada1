def estarVacio(pArchivo):
    contenido = pArchivo.readlines()
    for linea in contenido:
        if linea.strip() != "":
            return False
    return True

def existeReservada(pListaTokens, pToken):
    for tupla in pListaTokens:
        if pToken == tupla[0]:
            return True
    return False

def cargarTokensAux(pListaTokens):
    while True:
        nombreArchivo = input("Ingrese el nombre del archivo: ")
        try:
            with open(nombreArchivo, "r", encoding="utf-8") as archivo:
                if estarVacio(archivo):
                    return "El archivo ingresado está vacío"
                archivo.seek(0)
                while True:
                    separador = input("Ingrese el separador utilizado: ")
                    try:
                        return cargarTokens(pListaTokens, archivo, separador)
                    except:
                        print("El separador ingresado no es correcto")       
        except:
            print("El archivo ingresado no existe")

def cargarTokens(pListaTokens, nombreArchivo, separador):
    mensaje = False
    for linea in nombreArchivo:
        linea = linea.strip()
        if linea == "":
            continue
        if separador not in linea:
            if not mensaje:
                print("Uno o varios de los tokens ingresados no tienen separador o es incorrecto")
                mensaje = True
            continue
        partes = linea.split(separador)
        if len(partes) < 2:
            continue
        palabraReservada = partes[0].strip()
        reemplazo = partes[1].strip()
        if palabraReservada == "" or reemplazo == "":
            print(f"El token '{palabraReservada + " " + separador + " " + reemplazo}' no cumple con el formato adecuado")
            continue
        if not existeReservada(pListaTokens, palabraReservada):
            pListaTokens.append((palabraReservada, reemplazo))
        else:
            print(f"El token '{palabraReservada + " " + separador + " " + reemplazo}' ya existe en la base de datos")
    if len(pListaTokens) == 0:
        return "No se encontraron tokens válidos"
    if len(pListaTokens) > 1:
        print("Los demás tokens han sido agregados")
    return "¡Proceso realizado con éxito!"

def mostrarTokens(pListaTokens):
    if not estarVacia(pListaTokens):
        print("===========TOKENS CARGADOS===========")
        for tupla in pListaTokens:
            print(tupla[0], "->", tupla[1])
        return

def estarVacia(pListaTokens):
    if len(pListaTokens) == 0:
        print("El archivo ingreso se encuentra vacío")
        return True
    return False
    
def agregarModifAux(pListaTokens):
    textoTokens = input("Ingrese texto a procesar: ").strip()
    if textoTokens == "":
        return "La entrada no puede estar vacía"
    separador = input("Ingrese el separador utilizado en el texto: ").strip()
    if separador == "":
        print("El separador no puede estar vacío")
        return
    print("====================================")
    return agregarModif(pListaTokens, textoTokens, separador)

def agregarModif(pListaTokens, textoTokens, separador):
    tokens = textoTokens.split()
    for elemento in tokens:
        elemento = elemento.strip()
        if separador not in elemento:
            print(f"Token ignorado '{elemento}': no contiene el separador indicado")
            print("====================================")
            continue
        partes = elemento.split(separador)
        if len(partes) != 2:
            print(f"Token ignorado '{elemento}': formato incorrecto")
            print("====================================")
            continue
        palabraReservada = partes[0].strip()
        traduccion = partes[1].strip()
        if palabraReservada == "" or traduccion == "":
            print(f"Token ignorado '{elemento}': partes vacías")
            print("====================================")
            continue
        
        if existeReservada(pListaTokens, palabraReservada):
            print(f"¡El token '{palabraReservada + ' ' + separador + ' ' + traduccion}' se encontró en la base de datos!\nSe procederá a modificarlo")
            print("====================================")
            print(modificarToken(pListaTokens, palabraReservada))
            print("====================================")
        else:
            print(f"No se encontró el token '{palabraReservada + ' ' + separador + ' ' + traduccion}' en la base de datos\nSe procederá a agregarlo")
            print("====================================")
            print(agregarToken(pListaTokens, palabraReservada, traduccion))
            print("====================================")
    return "Proceso finalizado :)"

def existeTraduccion(pListaTokens, pToken):
    for tupla in pListaTokens:
        if pToken == tupla[1]:
            return True
    return False

def modificarToken(pListaTokens, pPalabraReservada):
        for i in range(len(pListaTokens)):
            tupla = pListaTokens[i]
            palabraReservada = tupla[0]
            if palabraReservada == pPalabraReservada:
                nuevoReemplazo = input("Ingrese el nuevo reemplazo: ").strip()
                if nuevoReemplazo == "":
                    return "El reemplazo no puede estar vacío"
                if existeTraduccion(pListaTokens, nuevoReemplazo):
                    return f"La traducción: '{nuevoReemplazo}' ya está siendo utilizada en otro token"
                pListaTokens[i] = (pPalabraReservada, nuevoReemplazo)
                print("====================================")
                return "¡El token ha sido modificado correctamente!"
        return "Token no encontrado"
               
def agregarToken(pListaTokens, pPalabraReservada, pTraduccion):
    nuevoToken = (pPalabraReservada, pTraduccion)
    pListaTokens.append(nuevoToken)
    return "¡El token se agregó correctamente!"

def guardarArchivoAux(pListaTokens):
        if estarVacia(pListaTokens):
            return "La base de datos se encuentra vacía"
        while True:
            nombreArchNuev = input("Ingrese el nombre del archivo a crear: ")
            if nombreArchNuev == "":
                print ("Debe de ingresar un nombre para el archivo")
                continue
            if not re.match(r"^[a-z0-9]+\.txt$", nombreArchNuev):
                print("El formato del nombre no es válido\nDebe de terminar en .txt")
                continue
            while True:
                separador = input("Ingrese el separador que desea usar: ")
                if separador == "" or separador == " ":
                    print ("El separador no puede estar vacío ni puede ser un espacio\n Por favor vuelva a intentarlo")
                    continue
                else:
                    with open(nombreArchNuev, "w", encoding="utf-8") as archivo:
                        return guardarArchivo(pListaTokens, archivo, separador)
                
def guardarArchivo(pListaTokens, pArchivo, pSeparador):
    for palabra, token in pListaTokens:
        linea = palabra + " " + pSeparador + " " + token + "\n"
        pArchivo.write(linea)
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

