def clases_fa_ord(clases, frecuencia):
    data = sorted(zip(clases, frecuencia))
    list_c, list_fa = zip(*data)
    return list_c, list_fa
    