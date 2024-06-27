def ord_data(clase, fa):
    data = sorted(zip(clase, fa))
    clases, frecuencia_a = zip(*data)
    return clases, frecuencia_a