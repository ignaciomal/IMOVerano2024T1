def clases_fa(arreglo):
    f_d = {}
    
    # Contar frecuencias de cada elemento
    for item in arreglo:
        if item in f_d:
            f_d[item] += 1
        else:
            f_d[item] = 1
            
    # Extraer clases y frecuencias en listas separadas
    clases = list(f_d.keys())
    frecuencias = list(f_d.values())
    
    return clases, frecuencias
            