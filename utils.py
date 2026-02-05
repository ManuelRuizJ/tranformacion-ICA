def validar_lista(valores):
    if not valores or len(valores) == 0:
        raise ValueError("Lista de valores vacía")
