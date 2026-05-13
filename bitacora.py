#Librerías utilizadas
import pickle
from datetime import datetime

#Funciones para manejar la bitácora de acciones realizadas en el programa
def cargarBitacora():
    """
    Función que carga la bitácora de acciones desde un archivo binario utilizando pickle
    Entrada: Ninguna
    Salida: list- Lista de registros de la bitácora, cada registro es una tupla con la fecha y la descripción de la acción
    """
    try:
        with open("bitacora.txt", "rb") as archivo:
            return pickle.load(archivo)
    except:
        return []

def guardarBitacora(pBitacora):
    """
    Función que guarda la bitácora de acciones en un archivo binario utilizando pickle
    Entrada: pBitacora(list)- Lista de registros de la bitácora, cada registro es una tupla con la fecha y la descripción de la acción
    Salida: None
    """    
    with open("bitacora.txt", "wb") as archivo:
        return pickle.dump(pBitacora, archivo)
        
def registrarAccion(pBitacora, pDescripcion):
    """
    Función que registra una acción realizada en el programa agregando un nuevo registro a la bitácora con la fecha actual y la descripción de la acción
    Entrada: pBitacora(list)- Lista de registros de la bitácora, cada registro es una tupla con la fecha y la descripción de la acción
             pDescripcion(str)- Descripción de la acción realizada
    Salida: None
    """
    fecha = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    registro = (fecha, pDescripcion)
    pBitacora.append(registro)
    return guardarBitacora(pBitacora)
    
def buscarPorFecha(pBitacora, pFecha):
    """
    Función que busca registros en la bitácora por fecha
    Entrada: pBitacora(list)- Lista de registros de la bitácora, cada registro es una tupla con la fecha y la descripción de la acción
             pFecha(str)- Fecha a buscar
    Salida: None
    """
    encontrado = False
    for fecha, descripcion in pBitacora:
        if pFecha in fecha:
            print(fecha, "->", descripcion)
            encontrado = True
    if not encontrado:
        print("No se encontraron registros")
    return
    
def buscarPorPalabra(pBitacora, pPalabra):
    """
    Función que busca registros en la bitácora por palabra clave en la descripción de la acción
    Entrada: pBitacora(list)- Lista de registros de la bitácora, cada registro es una tupla con la fecha y la descripción de la acción
             pPalabra(str)- Palabra clave a buscar en la descripción de la acción
    Salida: None
    """
    encontrado = False
    for fecha, descripcion in pBitacora:
        if pPalabra.lower() in descripcion.lower():
            print(fecha, "->", descripcion)
            encontrado = True
    if not encontrado:
        print("No se encontraron registros")
    return
