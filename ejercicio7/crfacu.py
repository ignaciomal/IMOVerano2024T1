def obt_fac(frecrel):
    facum = []
    acum = 0
    for i in frecrel:
        acum += i
        facum.append(acum)
    return facum