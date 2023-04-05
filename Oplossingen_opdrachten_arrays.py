'''
OPDRACHT 1
'''
# Voorbeeldopdracht voor variabelen en loops
getallen = [2, 4, 6, 8, 10]
resultaten = []

for nummer in getallen:
    kwadraat = nummer ** 2
    resultaten.append(kwadraat)

print("De lijst met kwadraten is:", resultaten)


'''
OPDRACHT 2
'''
# Voorbeeldopdracht voor lijsten en loops
namen = []

for i in range(5):
    naam = input("Voer een naam in: ")
    namen.append(naam)

print("De ingevoerde namen zijn:")
for naam in namen:
    print(naam)

'''
Opdracht 3
'''
# Voorbeeldopdracht voor lijsten en voorwaardelijke verklaringen
getallen = []
even = []
oneven = []

for i in range(5):
    nummer = int(input("Voer een getal in: "))
    getallen.append(nummer)
    if nummer % 2 == 0:
        even.append(nummer)
    else:
        oneven.append(nummer)

print("Alle getallen zijn:", getallen)
print("Even getallen zijn:", even)
print("Oneven getallen zijn:", oneven)

'''
OPDRACHT 4
'''
# Voorbeeldopdracht voor lijsten en strings
zin = input("Voer een zin in: ")
woorden = zin.split()

print("De woorden in de zin zijn:")
for woord in woorden:
    print(woord)

