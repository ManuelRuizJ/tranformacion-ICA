import pandas as pd

VALORES_INVALIDOS = ['---', '-9999', None]

def leer_excel_ruta(ruta_excel):
    df = pd.read_excel(ruta_excel, header=[0, 1, 2])

    # localizar columna fecha
    col_fecha = None
    for col in df.columns:
        if col[0] == "Fecha & Hora":
            col_fecha = col
            break

    if col_fecha is None:
        raise ValueError("No se encontró la columna 'Fecha & Hora'")

    filas = []

    for col in df.columns:
        estacion, contaminante, unidad = col

        if estacion == "Fecha & Hora":
            continue
        if contaminante == "Status":
            continue

        for _, row in df.iterrows():
            valor = row[col]
            fecha = row[col_fecha]

            if valor in VALORES_INVALIDOS:
                continue
            if isinstance(valor, str):
                continue
            if valor < 0:
                continue

            filas.append({
                "FechaHora": fecha,
                "Estacion": estacion.strip(),
                "Contaminante": contaminante.strip().upper(),
                "Unidad": unidad.strip(),
                "Valor": valor
            })

    return pd.DataFrame(filas)
