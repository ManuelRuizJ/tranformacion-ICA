from leer_excel import leer_excel_ruta
from utils import contaminante_valido, obtener_unidad
from utils import contaminante_valido, obtener_unidad, normalizar_contaminante

def main():
    ruta = "datos_calidad_aire.xlsx"
    df = leer_excel_ruta(ruta)

    print("\nContaminantes encontrados en el Excel:")
    print(df["Contaminante"].unique())


    df = df[df["Contaminante"].apply(contaminante_valido)]

    df["Unidad"] = df["Contaminante"].apply(obtener_unidad)

    df["FechaHora"] = df["FechaHora"].astype("datetime64[ns]")

    agurpado = df.groupby(
        ["Estacion", "Contaminante", "Unidad", "FechaHora"],
        as_index=False
    ).mean()

    print(agurpado.to_string(index=False))

    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
