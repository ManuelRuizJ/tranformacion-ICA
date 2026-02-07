from contaminantes import CONTAMINANTES

def contaminante_valido(nombre):
    return nombre in CONTAMINANTES
    
def obtener_unidad(nombre):
    return CONTAMINANTES[nombre]["unidad"]

def obtener_tipo_contaminante(nombre):
    return CONTAMINANTES[nombre]["promedio"]

def normalizar_contaminante(nombre):
    if not isinstance(nombre, str):
        return nombre

    n = nombre.strip().upper()

    reemplazos = {
        "PM2_5": "PM2.5",
        "PM 2.5": "PM2.5",
        "SO₂": "SO2",
        "NO₂": "NO2",
        "O₃": "O3",
    }

    return reemplazos.get(n, n)
