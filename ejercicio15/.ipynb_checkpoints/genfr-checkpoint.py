def gen_fr(frec_abs):
    datos = sum(frec_abs)
    fr = []
    for element in range(len(frec_abs)):
        fr.append((frec_abs[element] / datos) * 100)
    return fr