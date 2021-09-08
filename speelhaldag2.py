min = 45
persoon = 4
gmin = 5

tickets = 7.45
gameseat = 0.37

totaal = persoon * tickets + ((min / gmin) * gameseat * persoon)
koste =  totaal >= 44.44
print(koste)
if koste:
    print('Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar €44.44 euro’')
else:
    print('Het kost je meer dan €44.44!')
