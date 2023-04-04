'''
In het script waren een paar veel voorkomende fouten gemaakt. Hieronder kan je de verbeteringen zien door
het commentaar op te zoeken.

Zelfs wanneer de code wat complexer is, is het goed mogelijk om met Python fouten op te lossen.
'''
import random

class VirtueelHuisdier:
    def __init__(self, naam):
        self.naam = naam
        self.honger = 0
        self.vermoeidheid = 0 # Hier stond een : achter
        self.verveling = 0
        self.gezondheid = 100

    def voed(self):
        print(f"{self.naam} eet lekker zijn/haar eten op.")
        self.honger -= 10
        self.gezondheid += 5

    def speel(self):
        print(f"{self.naam} speelt vrolijk met zijn/haar speelgoed.")
        self.verveling -= 10
        self.vermoeidheid += 5
        self.gezondheid += 5

    def slaap(self):
        print(f"{self.naam} slaapt heerlijk.")
        self.vermoeidheid -= 10
        self.honger += 5
        self.gezondheid += 5

    def verzorg(self):
        print(f"{self.naam} voelt zich weer helemaal fris en fruitig na zijn/haar douche.")
        self.gezondheid += 10

    def toon_status(self): # Hier stond een 2 voor de functie. Functies mogen enkel met een _ of letter beginnen
        print(
            f"Naam: {self.naam}\nHonger: {self.honger}\nVermoeidheid: {self.vermoeidheid}\nVerveling: {self.verveling}\nGezondheid: {self.gezondheid}")

    def stap(self):
        self.honger += random.randint(1, 10)
        self.vermoeidheid += random.randint(1, 10)
        self.verveling += random.randint(1, 10)
        self.gezondheid -= random.randint(1, 10)

        if self.honger > 50:
            print(f"{self.naam} heeft honger!")

        if self.vermoeidheid > 50:
            print(f"{self.naam} is moe!")

        if self.verveling > 50:
            print(f"{self.naam} verveelt zich!")

        if self.gezondheid < 50:
            print(f"{self.naam} voelt zich niet zo goed...") # De functie print was niet goed afgesloten met een )

        if self.honger > 100:
            self.honger = 100

        if self.vermoeidheid > 100:
            self.vermoeidheid = 100

        if self.verveling > 100:
            self.verveling = 100

        if self.gezondheid < 0:
            self.gezondheid = 0


def main():
    naam = input("Geef je huisdier een naam: ")
    huisdier = VirtueelHuisdier(naam)
    keuze = None

    while keuze != "0":
        print(
            """
            Virtueel Huisdier Simulator

            0 - Afsluiten
            1 - Status tonen
            2 - Voeden
            3 - Spelen
            4 - Slapen
            5 - Verzorgen
            """
        )

        keuze = input("Wat wil je doen? ")

        if keuze == "1":
            huisdier.toon_status()

        elif keuze == "2":
            huisdier.voed()

        elif keuze == "3":
            huisdier.speel()

        elif keuze == "4":
            huisdier.slaap()

        elif keuze == "5":
            huisdier.verzorg()

        elif keuze == "0":
            print("Bedankt voor het spelen!") # Er zat een Typo in Print
            break

        else:
            print("Dat is geen geldige keuze. Probeer het opnieuw.")

        huisdier.stap()

if __name__ == '__main__':
    main()