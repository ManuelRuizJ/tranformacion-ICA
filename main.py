from contaminantes import CONTAMINANTES

def main():
    print("Calculadora del Índice AIRE Y SALUD (NOM-172)")

    contaminante = "PM25"
    print(f"Contaminante seleccionado: {contaminante}")

    info = CONTAMINANTES[contaminante]
    print("Información del contaminante:")
    print(info)

if __name__ == "__main__":
    main()
