def calcular_ICA(concentracion, bandas):
    for b in bandas:
        if b["c_min"] <= concentracion <= b["c_max"]:
            return interpolar(concentracion, b)
    return None

def interpolar(c, b):
    return( (b["ica_max"] - b["ica_min"]) / (b["c_max"] - b["c_min"]) ) * (c - b["c_min"]) + b["ica_min"]