#Elaborado por: Jimena Acuña Parra y Guideon Montero Vargas
#Fecha de elaboración: 18/04/2026 8:30pm
#Última fecha de modificación: 20/04/2026 10:08pm
#Versión: 3.14.3

#Importación de librerías
import tokens

#Definición de variables globales
listaTokens=[]

#Definición de la función principal
def menu():
    while True:
        print("===========MENÚ PRINCIPAL===========")
        print("1. Cargar tokens\n2. Mostrar tokens\n3. Agregar/modificar token\n4. Guardar tokens\n5. Traducir código\n6. Generar CSV\n7. Generar HTML\n8. Bitácora (submenú)\n9. Salir")
        opcion = (input("Seleccione una opción: "))
        if opcion == "1":
            print(tokens.cargarTokensAux(listaTokens))
        elif opcion == "2":
            tokens.mostrarTokens(listaTokens)
        elif opcion == "3":
            print(tokens.agregarModifAux(listaTokens))
        elif opcion == "4":
            print(tokens.guardarArchivoAux(listaTokens))
        elif opcion == "5":
            print(tokens.traducirTokensAux(listaTokens))
        elif opcion == "6":
            pass
        elif opcion == "7":
            pass
        elif opcion == "8":
            # otro menu
            pass
        elif opcion == "9":
            print("Saliendo del programa")
            break
        else:
            print("Opción Inválida")
#PP
menu()