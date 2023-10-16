aantal_personen = int(input("geef het aantal personen in"))
list_resultaten = []
for i in range(aantal_personen):
    naam = input("geef naam")
    geslacht = input("m of v")
    lopen = float(input("geef het aantal m lopen"))
    zwemmen = float(input("geef het aantal m zwemmen"))
    fietsen = int(input("geef het aantal km fietsen"))
    if geslacht == "m" and lopen > 20000 and zwemmen > 5000 and fietsen > 80:
        list_resultaten.append(str(naam+" Proficiat u bent Experte"))
    elif geslacht == "v" and lopen > 15000 and zwemmen > 4000 and fietsen > 70:
        list_resultaten.append(str(naam+" Proficiat u bent Expert"))
    elif geslacht == "m" and lopen > 15000 and zwemmen > 3000 and fietsen > 40:
        list_resultaten.append(str(naam+" Proficiat u bent Gevorderde"))
    elif geslacht == "v" and lopen > 12000 and zwemmen > 2000 and fietsen > 30:
        list_resultaten.append(str(naam+" Proficiat u bent Gevorderde"))
    else:
        list_resultaten.append(str(naam+" Nog oefenen"))

for res in list_resultaten:
    print(res)

