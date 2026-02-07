import pandas as pd

VALORES_INVALIDOS = ['---', '-9999', None]

def leer_excel_ruta(ruta_excel):
    df = pd.read_excel(ruta_excel, header=0)

    df.columns = [str(c).strip() for c in df.columns]

    filas = []

    for col in df.columns:
        if col in ["Fecha & Hora", "Fecha", "Hora"]:
            continue
        if "Status" in col:
            continue

        partes = col.split()
        if len(partes) < 2:
            continue

        estacion = partes[0]
        contaminante = partes[1]

        for _, row in df.iterrows():
            fecha = row["Fecha & Hora"]
            valor = row[col]

            if valor in VALORES_INVALIDOS:
                continue
            if isinstance(valor, str):
                continue
            if valor < 0:
                continue

            filas.append({
                "FechaHora": fecha,
                "Estacion": estacion,
                "Contaminante": contaminante,
                "Valor": valor
            })

        return pd.DataFrame(filas)