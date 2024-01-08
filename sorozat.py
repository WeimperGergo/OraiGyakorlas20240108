import random


def veletlenSzLista(szam1: int, szam2: int):
    print("II/a.", end="\n\t")
    vSzamok = []

    if szam2 < szam1:   # Ha a szám2 a kisebb, megcseréli őket.
        seged = szam1
        szam1 = szam2
        szam2 = seged

    rSzam = 0
    for i in range(1, 14, 1):
        rSzam = random.randint(szam1, szam2)
        vSzamok.append(rSzam)
        print(rSzam, end="%")
    print(rSzam)

    return vSzamok


def legkisebb(Lista):
    print("II/b.", end="\n\t")
    legKisebb = Lista[0]
    for i in range(0, len(Lista)):
        if legKisebb > Lista[i]:
            legKisebb = Lista[i]
    print(f"A legkisebb elem: {legKisebb}")

    fajlba = open("legkisebb.txt", "w", encoding="utf-8")
    fajlba.write(f"A legkisebb elem: {legKisebb}")
    fajlba.close()