from leer_excel import leer_excel_ruta
from utils import (
    contaminante_valido,
    obtener_unidad,
    normalizar_contaminante
)
from promedios import calcular_promedios
from exportar import exportar_excel
from clasificacion_ica import clasificar_ica
from ICA import (
    calcular_ICA_CO,
    calcular_ICA_O3,
    calcular_ICA_NO2,
    calcular_ICA_SO2,
    calcular_ICA_PM10
)


funciones_ica = {
    "CO": calcular_ICA_CO,
    "O3": calcular_ICA_O3,
    "NO2": calcular_ICA_NO2,
    "SO2": calcular_ICA_SO2,
    "PM10": calcular_ICA_PM10
}

def calcular_ica_fila(fila):
    contaminante = fila["Contaminante"]
    promedio = fila["Promedio"]
    return funciones_ica[contaminante](promedio)

def main():
    ruta = "datos/datos_calidad_aire.xlsx"

    df = leer_excel_ruta(ruta)

    print("\nDatos crudos:")
    print(df.head())

    df["Contaminante"] = df["Contaminante"].apply(normalizar_contaminante)
    df = df[df["Contaminante"].apply(contaminante_valido)]
    df["Unidad"] = df["Contaminante"].apply(obtener_unidad)

    print("\nDatos filtrados:")
    print(df.head())

    print("\nEstaciones encontradas:")
    print(df["Estacion"].unique())

    print("\nContaminantes encontrados:")
    print(df["Contaminante"].unique())

    df_prom = calcular_promedios(df)
    df_prom["ICA"] = df_prom.apply(calcular_ica_fila, axis=1)


    print("\nPromedios NOM-172:")
    print(df_prom.head(10))



    df_prom["ICA"] = df_prom.apply(calcular_ica_fila, axis=1)
    df_prom["Categoria"] = df_prom["ICA"].apply(clasificar_ica)

   
    exportar_excel(df_prom, "datos/salida_ICA_TOTAL.xlsx")



if __name__ == "__main__":
    main()
