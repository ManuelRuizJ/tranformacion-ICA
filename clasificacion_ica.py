def clasificar_ica(valor):
    if valor <= 50:
        return "Buena"
    elif valor <= 100:
        return "Regular"
    elif valor <= 150:
        return "Mala"
    elif valor <= 200:
        return "Muy mala"
    else:
        return "Extremadamente mala"

