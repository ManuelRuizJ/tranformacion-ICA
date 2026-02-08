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


def calcular_ICA_CO(co):
    if co <= 4.4:
        return co / 4.4 * 50
    elif co <= 9.4:
        return 50 + (co - 4.4) / (9.4 - 4.4) * 50
    elif co <= 12.4:
        return 100 + (co - 9.4) / (12.4 - 9.4) * 50
    elif co <= 15.4:
        return 150 + (co - 12.4) / (15.4 - 12.4) * 50
    else:
        return 200


def calcular_ICA_O3(o3):
    if o3 <= 54:
        return o3 / 54 * 50
    elif o3 <= 70:
        return 50 + (o3 - 54) / (70 - 54) * 50
    elif o3 <= 85:
        return 100 + (o3 - 70) / (85 - 70) * 50
    elif o3 <= 105:
        return 150 + (o3 - 85) / (105 - 85) * 50
    else:
        return 200


def calcular_ICA_NO2(no2):
    if no2 <= 53:
        return no2 / 53 * 50
    elif no2 <= 100:
        return 50 + (no2 - 53) / (100 - 53) * 50
    elif no2 <= 360:
        return 100 + (no2 - 100) / (360 - 100) * 50
    else:
        return 200


def calcular_ICA_SO2(so2):
    if so2 <= 35:
        return so2 / 35 * 50
    elif so2 <= 75:
        return 50 + (so2 - 35) / (75 - 35) * 50
    elif so2 <= 185:
        return 100 + (so2 - 75) / (185 - 75) * 50
    else:
        return 200


def calcular_ICA_PM10(pm10):
    if pm10 <= 54:
        return pm10 / 54 * 50
    elif pm10 <= 154:
        return 50 + (pm10 - 54) / (154 - 54) * 50
    elif pm10 <= 254:
        return 100 + (pm10 - 154) / (254 - 154) * 50
    else:
        return 200


