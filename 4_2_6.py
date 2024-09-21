def prod_escalar(v1,v2):
    if len(v1) != len(v2):
        return None
    pEscalar = 0
    for i in range(len(v1)):
        pEscalar += v1[i]*v2[i]
    return pEscalar
v1 = (1,2,3)
v2 = (1,2,3)
print(prod_escalar(v1,v2))