'''
De fout in dit script is dat we proberen een lijst van getallen en een float te combineren in de print-statements.
Hierdoor zal Python een foutmelding genereren vanwege onverenigbare typen.
Om deze fout te corrigeren, moeten we de lijst van getallen en het gemiddelde omzetten naar strings voordat we
deze proberen te combineren met andere strings. Dit kan worden gedaan door de functie str() te gebruiken.
Hieronder staat hetzelfde script met deze correctie.
'''

import random

print("Dit programma genereert een willekeurige getallenreeks en bepaalt het gemiddelde.")
n = int(input("Hoeveel getallen wil je genereren? "))
min = int(input("Wat is het minimum getal? "))
max = int(input("Wat is het maximum getal? "))

getallen = []

for i in range(n):
    getal = random.randint(min, max)
    getallen.append(getal)

gemiddelde = sum(getallen) / len(getallen)

print("De gegenereerde getallen zijn: " + str(getallen))
print("Het gemiddelde van de getallenreeks is: " + str(gemiddelde))
