import pandas as pd

def guardar_resultados(df_crudos, df_promedios, ruta_salida):
    with pd.ExcelWriter(ruta_salida, engine = "openpyxl") as writer:

        df_crudos.to_excel(writer, sheet_name = "Datos Limpios", index = False)

        df_promedios.to_excel(writer, sheet_name = "Promedios_NOM_172", index = False)