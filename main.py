import elagazas
import sorozat
import greenaway_m


# elagazas.hossz()

"""szamok = []
for i in range(2):
    szamok.append(int(input("Kérem adjon meg egy számot: ")))
sorozatLista = sorozat.veletlenSzLista(szamok[0], szamok[1])

sorozat.legkisebb(sorozatLista)"""

greenawayLista = greenaway_m.beolvas()
# greenaway_m.kiir(greenawayLista)
greenaway_m.filmekSzama(greenawayLista)
greenaway_m.vanSzakacs(greenawayLista)

