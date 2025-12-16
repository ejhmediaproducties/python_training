while True:
    # Vraag de gebruiker om invoer
    getal1 = input("Voer het eerste getal in (of STOP om te stoppen): ")

    # Controleer of de gebruiker wil stoppen
    if getal1 == "STOP":
        print("Bedankt, en tot ziens!")
        break

    getal1 = float(getal1)
    getal2 = float(input("Voer het tweede getal in: "))

    # Laat de gebruiker een bewerking kiezen
    print("Kies een bewerking:")
    print("1. Optellen (+)")
    print("2. Aftrekken (-)")
    print("3. Vermenigvuldigen (*)")
    print("4. Delen (/)")
    keuze = input("Voer het nummer van de gewenste bewerking in: ")

    # Voer de gekozen bewerking uit
    if keuze == "1":
        resultaat = getal1 + getal2
        bewerking = "optelling (+)"
    elif keuze == "2":
        resultaat = getal1 - getal2
        bewerking = "aftrekking (-)"
    elif keuze == "3":
        resultaat = getal1 * getal2
        bewerking = "vermenigvuldiging (*)"
    elif keuze == "4":
        if getal2 != 0:
            resultaat = getal1 / getal2
            bewerking = "deling (/)"
        else:
            print("Kan niet delen door nul.")
            continue
    else:
        print("Ongeldige keuze.")
        continue

    # Toon het resultaat
    print(f"{bewerking}: {getal1} {keuze} {getal2} = {resultaat}")
