import greenaway_o
from greenaway_o import Film


def beolvas():
    lista = []
    fajlbol = open("greenaway.txt", "r", encoding="utf-8")
    fajlbol.readline()      # Első sort nem tároljuk el
    sorok = fajlbol.readlines()     # Többi sor listába tárolása
    for i in range(0, len(sorok), 1):
        darabolt = sorok[i].strip().split("-")     # Tisztítás és darabolás
        konyvem = Film(darabolt[0], darabolt[1])
        lista.append(konyvem)
        # print(lista[i])
    fajlbol.close()
    # print(lista)
    return lista


"""def kiir(lista):
    for i in range(0, len(lista), 1):
        print(lista[i])"""


def filmekSzama(lista):
    fSzam = 0
    for i in range(0, len(lista), 1):
        fSzam += 1
    print(f"III/b.\n\tA filmek száma: {fSzam}")


def vanSzakacs(lista):
    print("III/d.")
    i = 0
    vanKeresett = False
    while i < len(lista):
        if "szakács" in lista[i].cim.lower() and vanKeresett == False:
            vanKeresett = True
        i += 1
    if vanKeresett:
        print("\tVan olyan film, amiben szerepel a \"szakács\" szó.")
    else:
        print("\tNincs olyan film, amiben szerepel a \"szakács\" szó.")
    #  \"  =  "
