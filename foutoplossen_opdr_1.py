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

print("De gegenereerde getallen zijn: " + getallen)
print("Het gemiddelde van de getallenreeks is: " + gemiddelde)
