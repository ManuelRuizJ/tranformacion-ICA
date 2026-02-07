def ppm_to_ug3(valor_ppm, peso_molecular):
    return (valor_ppm * peso_molecular * 1000) /24.45

def ppb_to_ug3(valor_ppb, peso_molecular):
    return(valor_ppb * peso_molecular) / 24.45