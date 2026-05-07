#Librerías utilizadas
import time
import re

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

def cargarTokensAux(pListaTokens):
    """
    Función auxiliar que solicita al usuario el nombre del archivo a cargar y el separador utilizado, y llama a la función cargarTokens para procesar el archivo
    Entrada: pListaTokens(list)- Lista de tokens
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
                    if cargarTokens(pListaTokens, archivo, separador):
                        return "¡Proceso realizado con éxito!"
                    else:
                        print("El separador ingresado no es correcto")
                        opcion = int(input("Ingrese:\n1-Volver a intentar\n2-Salir\nSu opción: "))
                        while opcion != 1 and opcion != 2:
                            print("Opcion invalida")
                            opcion = int(input("Ingrese:\n1-Volver a intentar\n2-Salir\nSu opción: "))
                        if opcion == 2:
                            return "Se volverá al menú principal"
        except:
            print("El archivo ingresado no existe")
            opcion = int(input("Ingrese:\n1-Volver a intentar\n2-Salir\nSu opción: "))
            while opcion != 1 and opcion != 2:
                print("Opcion invalida")
                opcion = int(input("Ingrese:\n1-Volver a intentar\n2-Salir\nSu opción: "))
            if opcion == 2:
                return "Se volverá al menú principal"

def cargarTokens(pListaTokens, nombreArchivo, separador):
    """
    Función que procesa un archivo de tokens y los agrega a la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens
             nombreArchivo(str)- Nombre del archivo a procesar
             separador(str)- Separador utilizado en el archivo
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
            print(f"El token '{palabraReservada + " " + separador + " " + reemplazo}' no cumple con el formato adecuado")
            continue
        if not existeReservada(pListaTokens, palabraReservada):
            pListaTokens.append((palabraReservada, reemplazo))
        else:
            print(f"El token '{palabraReservada + " " + separador + " " + reemplazo}' ya existe en la base de datos")
    return True

def mostrarTokens(pListaTokens):
    """
    Función que muestra los tokens cargados en la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens    
    Salida: None- Imprime los tokens cargados en la lista de tokens
    """
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
        print("El archivo ingreso se encuentra vacío")
        return True
    return False
    
def agregarModifAux(pListaTokens):
    """
    Función auxiliar que solicita al usuario el texto a procesar y el separador utilizado, y llama a la función agregarModif para procesar el texto
    Entrada: pListaTokens(list)- Lista de tokens
    Salida: str- Mensaje indicando el resultado del proceso
    """
    textoTokens = input("Ingrese texto a procesar: ").strip()
    if textoTokens == "":
        return "La entrada no puede estar vacía"
    separador = input("Ingrese el separador utilizado en el texto: ").strip()
    if separador == "":
        return "El separador no puede estar vacío"
    print("====================================")
    return agregarModif(pListaTokens, textoTokens, separador)

def agregarModif(pListaTokens, textoTokens, separador):
    """
    Función que agrega o modifica tokens en la lista de tokens según el texto ingresado por el usuario
    Entrada: pListaTokens(list)- Lista de tokens
             textoTokens(str)- Texto a procesar
             separador(str)- Separador utilizado en el texto
    Salida: str- Mensaje indicando el resultado del proceso
    """
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
            opcion = int(input(f"¡El token '{palabraReservada + ' ' + separador + ' ' + traduccion}' se encontró en la base de datos!\n¿Desea agregarlo?\n1- Si\n2- No\nOpcion: "))
            while opcion != 1 and opcion != 2:
                print("Opcion invalida")
                opcion = int(input(f"¡El token '{palabraReservada + ' ' + separador + ' ' + traduccion}' se encontró en la base de datos!\n¿Desea agregarlo?\n1- Si\n2- No\nOpcion: "))
            if opcion == 1:
                print("====================================")
                print(modificarToken(pListaTokens, palabraReservada))
                print("====================================")
            elif opcion == 2:
                print(f"No se modificara el token '{palabraReservada + ' ' + separador + ' ' + traduccion}'")
        else:
            print(f"No se encontró el token '{palabraReservada + ' ' + separador + ' ' + traduccion}' en la base de datos\nSe procederá a agregarlo")
            print("====================================")
            print(agregarToken(pListaTokens, palabraReservada, traduccion))
            print("====================================")
    return "Proceso finalizado :)"

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

def modificarToken(pListaTokens, pPalabraReservada):
    """
    Función que modifica un token en la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens
             pPalabraReservada(str)- Palabra reservada a modificar
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
            return "¡El token ha sido modificado correctamente!"
    return "Token no encontrado"

def agregarToken(pListaTokens, pPalabraReservada, pTraduccion):
    """
    Función que agrega un token a la lista de tokens
    Entrada: pListaTokens(list)- Lista de tokens
             pPalabraReservada(str)- Palabra reservada a agregar
             pTraduccion(str)- Traducción a agregar
    Salida: str- Mensaje indicando el resultado del proceso
    """
    nuevoToken = (pPalabraReservada, pTraduccion)
    pListaTokens.append(nuevoToken)
    return "¡El token se agregó correctamente!"

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
                print ("El separador no puede estar vacío ni puede ser un espacio\n Por favor vuelva a intentarlo")
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

def traducirTokensAux(pListaTokens, pResultado):
    """
    Función auxiliar que solicita al usuario el nombre del archivo a traducir y llama a la función traducirTokens para procesar el archivo
    Entrada: pListaTokens(list)- Lista de tokens
             pResultado(list)- Lista donde se guardarán las líneas traducidas
             pListaPalabras(list)- Lista donde se guardarán las palabras originales encontradas en el
             pListaConteo(list)- Lista donde se guardará el conteo de cada palabra original encontrada en el proceso de traducción
    Salida: str- Mensaje indicando el resultado del proceso
    """
    while True:
        nombreArchivo = pedirNombreArchivo()
        try:
            with open(nombreArchivo, "r", encoding="utf-8") as archivo:
                if estarVacio(archivo):
                    print("El archivo está vacío\nPor favor vuelva a intentarlo")
                    continue
        except:
            print("El archivo ingresado no existe\nPor favor vuelva a intentarlo")
            continue
        if estarVacia(pListaTokens):
            print ("Lo sentimos, no se encontraron tokens cargados")
            break
        while True:
            nombreNuevo = input("Ingrese el nombre del nuevo archivo: ").strip()
            if nombreNuevo == "":
                print("Nombre de archivo de salida inválido\nPor favor vuelva a intentarlo")
                continue
            try:
                with open(nombreArchivo, "r", encoding="utf-8") as archivo:
                    print("¡Proceso realizado con éxito!")
                    traducirTokens(pListaTokens, archivo, nombreNuevo, pResultado)
                    return nombreArchivo
            except:
                break

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
        nombreArchivo = input("Ingrese el nombre del archivo a traducir: ")
        if nombreArchivo == "":
            print("Nombre de archivo de salida inválido\nPor favor vuelva a intentarlo")
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
            palabras = linea.split()
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