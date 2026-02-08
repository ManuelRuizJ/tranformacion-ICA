import pandas as pd 

VENTANAS = {
    "O3": 8,
    "CO": 8,
    "PM10": 24,
    "PM25": 24,
    "NO2": 1,
    "SO2": 1,
}

def calcular_promedios(df):
    df = df.copy()

    df["FechaHora"] = pd.to_datetime(df["FechaHora"])

    resultados = []

    for (estaciones, contaminante), grupo in df.groupby(["Estacion", "Contaminante"]):
        ventana = VENTANAS.get(contaminante)

        if ventana is None:
            continue

        grupo = grupo.sort_values("FechaHora")

        if ventana == 1:
            grupo["Promedio"] = grupo["Valor"]
        else:
            grupo["Promedio"] = (
                grupo["Valor"].rolling(window = ventana, min_periods = ventana).mean()
            )

        grupo = grupo.dropna(subset = ["Promedio"])

        resultados.append(
            grupo[["FechaHora", "Estacion", "Contaminante", "Promedio"]]
        )

    if not resultados:
        return pd.DataFrame()
    
    return pd.concat(resultados, ignore_index = True)