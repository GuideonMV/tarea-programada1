#Librerías utilizadas
import time
import re
import bitacora

#Funciones para procesar tokens
def estarVacio(pArchivo):
    """
    Función que verifica si un archivo está vacío o no
    Entrada: Archivo(str)- Archivo a verficar
    Salida: bool- True si el archivo está vacío, False si no lo está
    """
    contenido = pArchivo.readlines()
    for linea in contenido:
        if linea.strip() != "":
            return False
    return True

def existeReservada(pListaTokens, pToken):
    """
    Función que verifica si una palabra reservada ya existe en la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens
             pToken(str)- Palabra reservada a verificar
    Salida: bool- True si la palabra reservada existe, False si no lo hace
    """
    for tupla in pListaTokens:
        if pToken == tupla[0]:
            return True
    return False

def cargarTokensAux(pListaTokens, pListaBitacora):
    """
    Función auxiliar que solicita al usuario el nombre del archivo a cargar y el separador utilizado, y llama a la función cargarTokens para procesar el archivo
    Entrada: pListaTokens(list)- Lista de tokens
             pListaBitacora(list)- Lista de acciones de bitácora
    Salida: str- Mensaje indicando el resultado del proceso
    """
    while True:
        nombreArchivo = input("Ingrese el nombre del archivo: ")
        try:
            with open(nombreArchivo, "r", encoding="utf-8") as archivo:
                if estarVacio(archivo):
                    print("El archivo ingresado está vacío")
                    continue
                while True:
                    archivo.seek(0)
                    separador = input("Ingrese el separador utilizado: ")
                    if cargarTokens(pListaTokens, archivo, separador, pListaBitacora):
                        return "¡Proceso realizado con éxito!"
                    else:
                        print("El separador ingresado no es correcto")
                        if desearContinuar() == 2:
                            return "Se volverá al menú principal"
        except:
            print("El archivo ingresado no existe")
            if desearContinuar() == 2:
                return "Se volverá al menú principal"

def cargarTokens(pListaTokens, nombreArchivo, separador, pListaBitacora):
    """
    Función que procesa un archivo de tokens y los agrega a la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens
             nombreArchivo(str)- Nombre del archivo a procesar
             separador(str)- Separador utilizado en el archivo
            pListaBitacora(list)- Lista de acciones de bitácora
    Salida: bool- True si el proceso se realiza con éxito, False si no
    """
    for linea in nombreArchivo:
        linea = linea.strip()
        if linea == "":
            continue
        partes = linea.split(separador)
        if separador not in linea:
            return False
        if len(partes) < 2:
            continue
        palabraReservada = partes[0].strip()
        reemplazo = partes[1].strip()
        if palabraReservada == "" or reemplazo == "":
            print(f"El token '{palabraReservada + ' ' + separador + ' ' + reemplazo}' no cumple con el formato adecuado")
            continue
        if not existeReservada(pListaTokens, palabraReservada):
            bitacora.registrarAccion(pListaBitacora, f"Se cargó el token '{palabraReservada+' ' + separador + ' ' + reemplazo}'")
            pListaTokens.append((palabraReservada, reemplazo))
        else:
            for i in range(len(pListaTokens)):
                if pListaTokens[i][0] == palabraReservada:
                    pListaTokens[i] = (palabraReservada, reemplazo)
                    bitacora.registrarAccion(pListaBitacora, f"Se actualizó el token '{palabraReservada}'")
                    break
    return True

def mostrarTokens(pListaTokens):
    """
    Función que muestra los tokens cargados en la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens    
    Salida: None- Imprime los tokens cargados en la lista de tokens
    """
    if estarVacia(pListaTokens):
        print("No hay tokens cargados en la base de datos")
        return
    if not estarVacia(pListaTokens):
        print("===========TOKENS CARGADOS===========")
        for tupla in pListaTokens:
            print(tupla[0], "->", tupla[1])
        return

def estarVacia(pListaTokens):
    """
    Función que verifica si la lista de tokens está vacía o no
    Entrada: pListaTokens(list)- Lista de tokens
    Salida: bool- True si la lista de tokens está vacía, False si no
    """
    if len(pListaTokens) == 0:
        return True
    return False
    
def agregarModifAux(pListaTokens, pListaBitacora):
    """
    Función auxiliar que solicita al usuario el texto a procesar y el separador utilizado, y llama a la función agregarModif para procesar el texto
    Entrada: pListaTokens(list)- Lista de tokens
             pListaBitacora(list)- Lista de acciones de bitácora
    Salida: str- Mensaje indicando el resultado del proceso
    """
    while True:
        textoTokens = input("Ingrese texto a procesar: ").strip()
        if textoTokens == "":
            print("La entrada no puede estar vacía")
            if desearContinuar() == 2:
                return "Volviendo al menú"
            continue
        while True:
            separador = input("Ingrese el separador utilizado en el texto: ").strip()
            if separador == "":
                print("El separador no puede estar vacío")
                if desearContinuar() == 2:
                    return "Volviendo al menú"
                continue
            print("====================================")
            return agregarModif(pListaTokens, textoTokens, separador, pListaBitacora)

def procesarTokenExistente(pListaTokens, palabraReservada, traduccion, separador, pListaBitacora):
    """
    Función que procesa un token existente para modificarlo en la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens
                palabraReservada(str)- Palabra reservada del token
                traduccion(str)- Traducción del token
                separador(str)- Separador utilizado en el token
                pListaBitacora(list)- Lista de acciones de bitácora
    Salida: str- Mensaje indicando el resultado del proceso
    """
    opcion = input(f"¡El token '{palabraReservada + ' ' + separador + ' ' + traduccion}' se encontró en la base de datos!\n¿Desea modificarlo?\n1- Si\n2- No\nOpcion: ")
    while opcion != "1" and opcion != "2":
        print("Opcion invalida")
        opcion = input(f"¡El token '{palabraReservada + ' ' + separador + ' ' + traduccion}' se encontró en la base de datos!\n¿Desea modificarlo?\n1- Si\n2- No\nOpcion: ")
    if opcion == "1":
        print("====================================")
        print(modificarToken(pListaTokens, palabraReservada, pListaBitacora))
        print("====================================")
    elif opcion == "2":
        print(f"No se modificara el token '{palabraReservada + ' ' + separador + ' ' + traduccion}'")

def procesarTokenNuevo(pListaTokens, palabraReservada, traduccion, separador, pListaBitacora):
    """
    Función que procesa un token nuevo para agregarlo a la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens
             palabraReservada(str)- Palabra reservada del token
             traduccion(str)- Traducción del token
             separador(str)- Separador utilizado en el token
             pListaBitacora(list)- Lista de acciones de bitácora
    Salida: str- Mensaje indicando el resultado del proceso
    """
    print(f"No se encontró el token '{palabraReservada + ' ' + separador + ' ' + traduccion}' en la base de datos\n¿Desea agregarlo?")
    opcion = input("Ingrese:\n1- Si\n2- No\nSu opción: ")
    while opcion != "1" and opcion != "2":
        print("Opcion invalida")
        opcion = input("Ingrese:\n1- Si\n2- No\nSu opción: ")
    if opcion == "1":
        print("====================================")
        agregarToken(pListaTokens, palabraReservada, traduccion, pListaBitacora)
        print(f"¡El token '{palabraReservada + ' ' + separador + ' ' + traduccion}' ha sido agregado correctamente!")
    elif opcion == "2":
        print(f"No se agregará el token '{palabraReservada + ' ' + separador + ' ' + traduccion}'")
    print("====================================")

def agregarModif(pListaTokens, textoTokens, pSeparador, pListaBitacora):
    """
    Función que procesa un texto ingresado por el usuario para agregar o modificar tokens en la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens
             textoTokens(str)- Texto a procesar
             pSeparador(str)- Separador utilizado en el texto
             pListaBitacora(list)- Lista de acciones de bitácora
    Salida: str- Mensaje indicando el resultado del proceso
    """
    tokens = textoTokens.split()
    for elemento in tokens:
        elemento = elemento.strip()
        if pSeparador not in elemento:
            print(f"Token ignorado '{elemento}': no contiene el separador indicado")
            print("====================================")
            continue
        partes = elemento.split(pSeparador)
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
            procesarTokenExistente(pListaTokens, palabraReservada, traduccion, pSeparador, pListaBitacora)
        else:
            procesarTokenNuevo(pListaTokens, palabraReservada, traduccion, pSeparador, pListaBitacora)
    return "Proceso finalizado con éxito"

def existeTraduccion(pListaTokens, pToken):
    """
    Función que verifica si una traducción ya existe en la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens
             pToken(str)- Traducción a verificar
    Salida: bool- True si la traducción existe, False si no
    """
    for tupla in pListaTokens:
        if pToken == tupla[1]:
            return True
    return False

def modificarToken(pListaTokens, pPalabraReservada, pListaBitacora):
    """
    Función que modifica un token en la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens
             pPalabraReservada(str)- Palabra reservada a modificar
             pListaBitacora(list)- Lista de acciones de bitácora
    Salida: str- Mensaje indicando el resultado del proceso
    """
    for i in range(len(pListaTokens)):
        tupla = pListaTokens[i]
        palabraReservada = tupla[0]
        if palabraReservada == pPalabraReservada:
            nuevoReemplazo = input("Ingrese el nuevo reemplazo: ").strip().lower()
            if nuevoReemplazo == "":
                return "El reemplazo no puede estar vacío"
            if existeTraduccion(pListaTokens, nuevoReemplazo):
                return f"La traducción: '{nuevoReemplazo}' ya está siendo utilizada en otro token"
            pListaTokens[i] = (pPalabraReservada, nuevoReemplazo)
            print("====================================")
            bitacora.registrarAccion(pListaBitacora, f"Se modificó el token '{pPalabraReservada}'")
            return "¡El token ha sido modificado correctamente!"
    return "Token no encontrado"

def agregarToken(pListaTokens, pPalabraReservada, pTraduccion, pListaBitacora):
    """
    Función que agrega un token a la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens
             pPalabraReservada(str)- Palabra reservada a agregar
             pTraduccion(str)- Traducción a agregar
    Salida: str- Mensaje indicando el resultado del proceso
    """
    nuevoToken = (pPalabraReservada, pTraduccion)
    pListaTokens.append(nuevoToken)
    bitacora.registrarAccion(pListaBitacora, f"Se agregó el token '{pPalabraReservada}'")
    return

def guardarArchivoAux(pListaTokens):
    """
    Función que guarda la lista de tokens en un archivo
    Entrada: pListaTokens(list)- Lista de tokens
    Salida: str- Mensaje indicando el resultado del proceso
    """
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
                print ("El separador no puede estar vacío ni puede ser un espacio, por favor vuelva a intente de nuevo")
                continue
            else:
                with open(nombreArchNuev, "w", encoding="utf-8") as archivo:
                    return guardarArchivo(pListaTokens, archivo, separador)

def guardarArchivo(pListaTokens, pArchivo, pSeparador):
    """"
    Función que guarda la lista de tokens en un archivo con el formato adecuado
    Entrada: pListaTokens(list)- Lista de tokens
             pArchivo(file)- Archivo donde se guardarán los tokens
             pSeparador(str)- Separador utilizado en el archivo
    Salida: str- Mensaje indicando el resultado del proceso
    """
    for palabra, token in pListaTokens:
        linea = palabra + " " + pSeparador + " " + token + "\n"
        pArchivo.write(linea)
    print("====================================")
    return "¡Archivo guardado correctamente!"

def validarArchivoEntrada(pNombreArchivo):
    """
    Función que valida que el archivo de entrada para la traducción exista y no esté vacío
    Entrada: pNombreArchivo(str)- Nombre del archivo a traducir
    Salida: bool- True si el archivo es válido, False si no lo es
    """
    try:
        with open(pNombreArchivo, "r", encoding="utf-8") as archivo:
            if estarVacio(archivo):
                print("El archivo ingresado está vacío")
                return False
        return True
    except:
        print("El archivo ingresado no existe")
        return False

def pedirArchivoSalida(pListaTokens, pNombreArchivo, pResultado):
    """
    Función que solicita al usuario el nombre del archivo de salida para guardar el resultado de la traducción
    Entrada: pListaTokens(list)- Lista de tokens
             pNombreArchivo(str)- Nombre del archivo a traducir
             pResultado(list)- Lista donde se guardarán las líneas traducidas
    Salida: str- Mensaje indicando el resultado del proceso
    """
    while True:
        nombreNuevo = input("Ingrese el nombre del nuevo archivo: ").strip()
        if nombreNuevo == "":
            print("Nombre de archivo de salida inválido")
            continue
        with open(pNombreArchivo, "r", encoding="utf-8") as archivo:
            print("¡Proceso realizado con éxito!")
            traducirTokens(pListaTokens, archivo, nombreNuevo, pResultado)
            return pNombreArchivo

def traducirTokensAux(pListaTokens, pResultado):
    """
    Función auxiliar que traduce los tokens en un archivo y guarda el resultado
    Entrada: pListaTokens(list)- Lista de tokens
             pResultado(list)- Lista donde se guardarán las líneas traducidas
    Salida: str- Mensaje indicando el resultado del proceso
    """
    if estarVacia(pListaTokens):
        print("Lo sentimos, no se encontraron tokens cargados")
        return None
    while True:
        pResultado.clear()
        nombreArchivo = pedirNombreArchivo()
        if nombreArchivo is None:
            return None
        if not validarArchivoEntrada(nombreArchivo):
            if desearContinuar() == 2:
                return None
            continue
        return pedirArchivoSalida(pListaTokens, nombreArchivo, pResultado)

def traducirTokens(pListaTokens, pArchivo, pNombreNuevo, pResultado):
    """
    Función que traduce el código de un archivo utilizando la lista de tokens y guarda el resultado en un nuevo archivo
    Entrada: pListaTokens(list)- Lista de tokens
             pArchivo(file)- Archivo a traducir
             pNombreNuevo(str)- Nombre del nuevo archivo donde se guardará el resultado
             pResultado(list)- Lista donde se guardarán las líneas traducidas
    Salida: str- Mensaje indicando el resultado del proceso
    """
    for linea in pArchivo:
        espacios = len(linea) - len(linea.lstrip())
        contenido = linea.strip()
        partes = re.split(r'(\W)', contenido)
        nueva = []
        for parte in partes:
            if parte.isdigit():
                nueva.append(parte)
                continue
            reemplazado = False
            for original, traduccion in pListaTokens:
                if parte == original:
                    nueva.append(traduccion)
                    reemplazado = True
                    break
            if not reemplazado:
                nueva.append(parte)
        nuevaLinea = " " * espacios + "".join(nueva)
        pResultado.append(nuevaLinea)
    with open(pNombreNuevo, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(pResultado))
    return pResultado

def pedirNombreArchivo():
    """
    Función que solicita al usuario el nombre del archivo a traducir
    Entrada: None
    Salida: str- Nombre del archivo a traducir
    """
    while True:
        nombreArchivo = input("Ingrese el nombre del archivo a traducir: ").strip()
        if nombreArchivo == "":
            print("Nombre de archivo inválido")
            if desearContinuar() == 2:
                return None 
            continue  
        return nombreArchivo

def contarReemplazos(pListaTokens, pResultado):
    """
    Función que cuenta la cantidad de veces que se reemplazó cada palabra original en el proceso de traducción
    Entrada: pListaTokens(list)- Lista de tokens
             pResultado(list)- Lista de líneas traducidas
    Salida: tuple- Tupla con el conteo de cada palabra original y el total de reemplazos
    """
    conteo = []
    total = 0
    for original, traduccion in pListaTokens:
        cantidad = 0
        for linea in pResultado:
            palabras = re.split(r'(\W)', linea)
            for palabra in palabras:
                if palabra == traduccion:
                    cantidad += 1
        conteo.append((original, traduccion, cantidad))
        total += cantidad
    return conteo, total

def contarPalabras(pNombreArchivo):
    """
    Función que cuenta la cantidad de palabras en un archivo
    Entrada: pNombreArchivo(str)- Nombre del archivo a contar
    Salida: int- Cantidad de palabras en el archivo
    """
    totalPalabras = 0
    with open(pNombreArchivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            palabras = linea.split()
            totalPalabras += len(palabras)
    return totalPalabras

def procesarTiempo(pInicio):
    """
    Función que calcula la duración de un proceso dado su tiempo de inicio
    Entrada: pInicio(float)- Tiempo de inicio del proceso
    Salida: float- Duración del proceso en segundos
    """
    fin = time.time()
    duracion = fin - pInicio
    return duracion

def generarCsvAux(pResultado, pConteo):
    """
    Función auxiliar que solicita al usuario el nombre del archivo CSV a generar y llama a la función generarCsv para procesar el conteo de reemplazos
    Entrada: pResultado(list)- Lista de líneas traducidas
             pConteo(list)- Lista con el conteo de cada palabra original y su traducción
    Salida: str- Mensaje indicando el resultado del proceso
    """
    if len(pResultado) == 0 or len(pConteo) == 0:
        return "No se han realizado traducciones aún, no hay datos para generar el CSV"
    nombreArchivo = input("Ingrese el nombre del archivo CSV: ").strip()
    while True:
        if nombreArchivo == "":
            print("Nombre inválido")
            nombreArchivo = input("Ingrese el nombre del archivo CSV: ").strip()
        elif not nombreArchivo.endswith(".csv"):
            print("El archivo debe terminar en .csv")
            nombreArchivo = input("Ingrese el nombre del archivo CSV: ").strip()
        else:
            return generarCsv(pConteo, nombreArchivo)

def generarCsv(pConteo, pNombreArchivo):
    """
    Función que genera un archivo CSV con el conteo de reemplazos de cada palabra original
    Entrada: pConteo(list)- Lista con el conteo de cada palabra original y su traducción
             pNombreArchivo(str)- Nombre del archivo CSV a generar
    Salida: str- Mensaje indicando el resultado del proceso
    """
    datos = list(pConteo)
    for i in range(len(datos)):
        for j in range(i + 1, len(datos)):
            if datos[j][2] > datos[i][2]:
                datos[i], datos[j] = datos[j], datos[i]
    try:
        with open(pNombreArchivo, "w", encoding="utf-8") as archivo:
            archivo.write("Original;Reemplazo;Cantidad\n")
            for original, traduccion, cantidad in datos:
                archivo.write(f"{original};{traduccion};{cantidad}\n")
        return "¡CSV generado correctamente!"
    except PermissionError:
        return "Cierra el archivo antes de ejecutarlo"

def desearContinuar():
    """
    Función que pregunta al usuario si desea continuar con el proceso
    Entrada: None
    Salida: int- Opción seleccionada por el usuario
    """
    opcion = input("Ingrese:\n1-Volver a intentar\n2-Salir\nSu opción: ")
    while opcion != "1" and opcion != "2":
        print("Opcion invalida")
        opcion = input("Ingrese:\n1-Volver a intentar\n2-Salir\nSu opción: ")
    return int(opcion)