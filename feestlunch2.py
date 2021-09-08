anc = 17
ans = 2
ank = 3

croissantje = 0.39
stokbroden = 2.78
kortingsbonnen = 0.50

totaal = anc * croissantje + (ans * stokbroden) - (ank * kortingsbonnen)
koste = totaal >= 18.88
print(koste)
if koste:
    print('De feestlunch kost je bij de bakker 18.88 euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')
else:
    print('kortingen zijn niet geldig!')