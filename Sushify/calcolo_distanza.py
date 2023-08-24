import math

def cosine_similarity_mod(point_a, point_b):
    """funzione che calcola da distanza vettoriale cosine tra due punti, restituisce 0 se i due punti hanno dimensioni diverse"""
    if len(point_a) != len(point_b):
        return 0

    numeratore = 0
    denominatore = 1 # uno affinchè non ci sia 0 al denominatore

    for i in range(0,len(point_a)):
        numeratore = numeratore + (point_a[i] * point_b[i])
        denominatore = denominatore + (point_a[i]**2 * point_b[i]**2)

    return numeratore / denominatore

def euclide_similarity_mod(point_a, point_b):
    """funzione che calcola da distanza euclidea (vicinato sferico) tra due punti, restituisce 0 se i due punti hanno dimensioni diverse"""
    if len(point_a) != len(point_b):
        return 0

    distanza = 0

    for i in range(0,len(point_a)):
        distanza = distanza + (point_a[i] - point_b[i])**2

    return math.sqrt(distanza)
