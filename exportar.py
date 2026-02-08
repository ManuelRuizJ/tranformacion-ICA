import pandas as pd

def exportar_excel(df, nombre_archivo):
    """Exporta un DataFrame a Excel usando openpyxl como engine.

    Args:
        df (pd.DataFrame): DataFrame a exportar.
        nombre_archivo (str): Ruta de salida del archivo .xlsx.
    """
    with pd.ExcelWriter(nombre_archivo, engine = "openpyxl") as writer:
        df.to_excel(writer, index = False, sheet_name = "ICA")

import pandas as pd

def exportar_excel(df, nombre_archivo):
    with pd.ExcelWriter(nombre_archivo, engine = "openpyxl") as writer:
        df.to_excel(writer, index = False, sheet_name = "ICA")