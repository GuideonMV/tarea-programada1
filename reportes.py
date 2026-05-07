from datetime import datetime
def generarHTML(pListaTokens, pDuracion, pTotalPalabras, pTotalReemplazos, pConteo):
    ahora = datetime.now()
    nombreArchivo = ahora.strftime("reporteHTML_%d-%m-%y_%H-%M-%S.html")
    fecha = ahora.strftime("%d/%m/%y-%H:%M:%S")
    titulo = input("Ingrese el título del reporte: ")
    if pTotalPalabras > 0:
        porcentaje = (pTotalReemplazos / pTotalPalabras) * 100
    else:
        porcentaje = 0
    filas = ""
    i = 0
    for original, reemplazo, cantidad in pConteo:
        if i % 2 == 0:
            color = "#f2f2f2"
        else:
            color = "#ffffff"
        filas += f'<tr style="background-color:{color};"><td>{original}</td><td>{reemplazo}</td><td>{cantidad}</td></tr>\n'
        i += 1
    contenido = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>
</head>
<body>
    <header>
        <h1>Reporte de Traducción</h1>
    </header>
    <section>
        <h2>Fecha y hora de generación: {fecha}</h2>
        <p>Duración total de procesamiento: {round(pDuracion, 2)}</p>
        <p>Total de palabras reemplazadas: {pTotalReemplazos}</p>
        <p>Porcentaje de palabras reemplazadas: {round(porcentaje, 2)}%</p>
    </section>
    <table>
        <tr>
            <th style="text-align:center;">Palabra Original</th>
            <th style="text-align:center;">Reemplazo</th>
            <th style="text-align:center;">Cantidad de reemplazos</th>
        </tr>
        {filas}
    </table>
</body>
</html>
"""
    archivo = open(nombreArchivo, "x", encoding="utf-8")
    archivo.write(contenido)
    archivo.close()
    print("¡Reporte HTML generado correctamente!")