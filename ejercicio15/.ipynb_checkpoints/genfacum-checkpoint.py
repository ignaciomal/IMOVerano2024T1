def fec_acum(frecuencia_rel):
    facum = []
    conteo = 0
    for e in frecuencia_rel:
        conteo += e
        facum.append(conteo)
    return facum