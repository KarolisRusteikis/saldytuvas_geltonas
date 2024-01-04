""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas
* Spausdinti pajamų/išlaidų žurnalą
* Suskaičiuoti biudžeto balansą

"""

# Biudžeto žurnalo žodynas, kuris saugo pajamas ir išlaidas
# Raktas - paskirtis, Reikšmė - pajamos (teigiamas float) arba išlaidos (neigiamas float)


# Biudžeto žurnalo žodynas, kuris saugo pajamas ir išlaidas
# Raktas - paskirtis, Reikšmė - pajamos (teigiamas float) arba išlaidos (neigiamas float)
biudzeto_zurnalas = {}

def prideti_pajamas(paskirtis, suma):
    """
    Funkcija prideda pajamas į biudžeto žurnalą.

    :param paskirtis: Pajamų paskirtis.
    :param suma: Pajamų suma (teigiamas float).
    """
    # Patikrina, ar paskirtis jau yra žurnale, jei ne - prideda naują įrašą
    if paskirtis not in biudzeto_zurnalas:
        biudzeto_zurnalas[paskirtis] = 0
    # Prideda pajamas prie esamos sumos
    biudzeto_zurnalas[paskirtis] += suma

def prideti_islaidas(paskirtis, suma):
    """
    Funkcija prideda išlaidas į biudžeto žurnalą.

    :param paskirtis: Išlaidų paskirtis.
    :param suma: Išlaidų suma (neigiamas float).
    """
    # Patikrina, ar paskirtis jau yra žurnale, jei ne - prideda naują įrašą
    if paskirtis not in biudzeto_zurnalas:
        biudzeto_zurnalas[paskirtis] = 0
    # Prideda išlaidas prie esamos sumos (neigiamas skaičius)
    biudzeto_zurnalas[paskirtis] -= suma

def spausdinti_zurnala():
    """
    Funkcija spausdina biudžeto žurnalą, įskaitant pajamas ir išlaidas.
    """
    print("===[ Pajamų/Išlaidų žurnalas ]===")
    # Iteruoja per biudžeto žurnalo įrašus naudodamas .items()
    for paskirtis, suma in biudzeto_zurnalas.items():
        # Spausdina paskirtį ir sumą su dviem skaitmenimis po kablelio
        print(f"{paskirtis}: {suma:.2f}")
    print("===============================")

def skaiciuoti_balansa():
    """
    Funkcija suskaičiuoja ir spausdina biudžeto balansą.
    """
    # Suskaičiuoja biudžeto balansą kaip sumą visų pajamų ir išlaidų
    # naudojant sum() funkciją
    balansas = sum(biudzeto_zurnalas.values())
    # Spausdina biudžeto balansą su dviem skaitmenimis po kablelio
    print(f"Biudžeto balansas: {balansas:.2f}")

def main():
    while True:
        print("=======================")
        print("|---[MONEY COUNTER]---|")
        print("=======================")
        print("\n1. Pridėti pajamas")
        print("2. Pridėti išlaidas")
        print("3. Spausdinti pajamų/išlaidų žurnalą")
        print("4. Suskaičiuoti biudžeto balansą")
        print("5. Baigti programą")

        pasirinkimas = input("Pasirinkite veiksmą (1-5): ")

        if pasirinkimas == '1':
            paskirtis = input("Įveskite pajamų paskirtį: ")
            suma = float(input("Įveskite pajamų sumą: "))
            prideti_pajamas(paskirtis, suma)
        elif pasirinkimas == '2':
            paskirtis = input("Įveskite išlaidų paskirtį: ")
            suma = float(input("Įveskite išlaidų sumą: "))
            prideti_islaidas(paskirtis, suma)
        elif pasirinkimas == '3':
            spausdinti_zurnala()
        elif pasirinkimas == '4':
            skaiciuoti_balansa()
        elif pasirinkimas == '5':
            print("Programa baigta.")
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")


if __name__ == "__main__":
    main()
