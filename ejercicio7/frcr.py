def obt_fr(fa):
    datos = sum(fa)
    
    frec_rel = []
    
    for i in range(len(fa)):
        frec_rel.append((fa[i]  / datos) * 100)
        
    return frec_rel