'''
De fout in dit script is dat de input-functie waarmee getallen worden ingevoerd, deze altijd als strings retourneert.
Hierdoor is de volgende regel (gemiddelde = (getal1 + getal2) / 2) ongeldig omdat we niet kunnen delen door strings.
Om deze fout te corrigeren, moeten we de ingevoerde strings omzetten naar numerieke waarden (bijv. floats)
met de functie float(). Hieronder staat hetzelfde script met deze correctie.
'''

print("Dit programma zal het gemiddelde berekenen van twee getallen.")

# Laat de gebruiker twee getallen invoeren
getal1 = float(input("Voer het eerste getal in: "))
getal2 = float(input("Voer het tweede getal in: "))

# Bereken het gemiddelde uit
gemiddelde = (getal1 + getal2) / 2

# geef het gemiddelde weer terug
print("Het gemiddelde van " + str(getal1) + " en " + str(getal2) + " is " + str(gemiddelde) + ".")
