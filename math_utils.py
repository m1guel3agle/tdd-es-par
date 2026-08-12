def es_par(n):
    return n % 2 == 0


def es_impar(n):
    return n % 2 != 0


def es_positivo(n):
    return n > 0


def es_negativo(n):
    return n < 0

def es_multiplo_de(n, m):
    if m == 0:
        return False
    return n % m == 0