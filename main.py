from leer_excel import leer_excel_ruta
from utils import contaminante_valido, obtener_unidad, normalizar_contaminante
from promedios import calcular_promedios
from exportar_excel import guardar_resultados

def main():
    ruta = "datos_calidad_aire.xlsx"

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

    print("\nPromedios NOM-172:")
    print(df_prom.head(10))

        # Ruta del Excel de salida
    ruta_salida = "resultados_ICA.xlsx"

    guardar_resultados(
        df_crudos=df,
        df_promedios=df_prom,
        ruta_salida=ruta_salida
    )

    print("\nArchivo Excel generado:", ruta_salida)




if __name__ == "__main__":
    main()
