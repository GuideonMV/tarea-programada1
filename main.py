#Elaborado por: Jimena Acuña Parra y Guideon Montero Vargas
#Fecha de elaboración: 18/04/2026 8:30pm
#Última fecha de modificación: 20/04/2026 10:08pm
#Versión: 3.14.3

#Importación de librerías
import tokens
import reportes
import bitacora
import time

#Definición de variables globales
listaTokens = []
lineasTraducidas = []
conteo = []
listaBitacora = bitacora.cargarBitacora()
#Definición de la función principal
def menu():
    global conteo, totalReemplazos, duracion, totalPalabras
    while True:
        print("===========MENÚ PRINCIPAL===========")
        print("1. Cargar tokens")
        print("2. Mostrar tokens")
        print("3. Agregar/modificar token")
        print("4. Guardar tokens")
        print("5. Traducir código")
        print("6. Generar CSV")
        print("7. Generar HTML")
        print("8. Bitácora")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            bitacora.registrarAccion(listaBitacora,
            "Se ejecutó la opción cargar tokens")
            print(tokens.cargarTokensAux(listaTokens))
        elif opcion == "2":
            bitacora.registrarAccion(listaBitacora,
            "Se ejecutó la opción mostrar tokens")
            tokens.mostrarTokens(listaTokens)
        elif opcion == "3":
            bitacora.registrarAccion(listaBitacora,
            "Se ejecutó la opción agregar/modificar token")
            print(tokens.agregarModifAux(listaTokens))
        elif opcion == "4":
            bitacora.registrarAccion(listaBitacora,
            "Se ejecutó la opción guardar tokens")
            print(tokens.guardarArchivoAux(listaTokens))
        elif opcion == "5":
            bitacora.registrarAccion(listaBitacora,
            "Se ejecutó la opción traducir código")
            inicio = time.time()
            nombreArchivo = tokens.traducirTokensAux(listaTokens, lineasTraducidas)
            duracion = tokens.procesarTiempo(inicio)
            totalPalabras = tokens.contarPalabras(nombreArchivo)
            conteo, totalReemplazos = tokens.contarReemplazos(listaTokens, lineasTraducidas)
        elif opcion == "6":
            bitacora.registrarAccion(listaBitacora,
            "Se ejecutó la opción generar CSV")
            print(tokens.generarCsvAux(listaTokens, conteo))
        elif opcion == "7":
            bitacora.registrarAccion(listaBitacora,
            "Se ejecutó la opción generar HTML")
            reportes.generarHTML(listaTokens, duracion,
            totalPalabras, totalReemplazos, conteo)
        elif opcion == "8":
            bitacora.registrarAccion(listaBitacora,
            "Se ingresó al submenú de bitácora")
            while True:
                print("===========BITÁCORA===========")
                print("A) Acciones por día escogido")
                print("B) Acciones por palabra clave")
                print("C) Salir")
                opcion2 = input("Seleccione una opción: ").lower()
                if opcion2 == "a":
                    fecha = input("Ingrese la fecha (AAAA-MM-DD): ")
                    bitacora.buscarPorFecha(listaBitacora, fecha)
                elif opcion2 == "b":
                    palabra = input("Ingrese la palabra clave: ")
                    bitacora.buscarPorPalabra(listaBitacora, palabra)
                elif opcion2 == "c":
                    bitacora.registrarAccion(listaBitacora,
                    "Se salió del submenú de bitácora")
                    break
                else:
                    print("Opción inválida")
        elif opcion == "9":
            bitacora.registrarAccion(listaBitacora,"El usuario salió del programa")
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida")
#PP
menu()