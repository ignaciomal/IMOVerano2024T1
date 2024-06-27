def gen_class_fa(arr):
    
    frecuencia_dict = {}
    
    
    for item in arr:
        if item in frecuencia_dict:
            frecuencia_dict[item] += 1
        else:
            frecuencia_dict[item] = 1
            
    
    clases = list(frecuencia_dict.keys())
    frecuencias = list(frecuencia_dict.values())
    
    return clases, frecuencias