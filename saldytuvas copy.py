""" Komandinio darbo užduotis
===[ Šaldytuvas ]===

Reikalavimai:

* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float).
* Pridėti produktą į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais.
* Išimti produktą iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas.
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve.
* Išspausdinti visą šaldytuvo turinį su kiekiais.

BONUS:

* Patikrinti, ar receptas išeina. 
** Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
** Jeigu receptas neišeina, išvardinti kiek ir kokių produktų trūksta.

"""


fridge_content = {}

def add_product(produktas, kiekis):
    fridge_content[produktas] = fridge_content.get(produktas, 0) + kiekis
    print(f"Šaldytuve yra: {fridge_content}")

def remove_product(produktas, kiekis):
    if produktas in fridge_content:
        fridge_content[produktas] -= kiekis
        if fridge_content[produktas] <= 0:
            del fridge_content[produktas]
        print(f"Iš šaldytuvo išimta: {kiekis} {produktas}")
        print(f"Šaldytuve dabar yra: {fridge_content}")
    else:
        print(f"Šaldytuve nėra: {produktas}.")

def check_product_quantity(produktas, reikalingas_kiekis):
    if produktas in fridge_content and fridge_content[produktas] >= reikalingas_kiekis:
        print(f"Šaldutyve yra pakankamai: {produktas}")
    else:
        print(f"Šaldytuve nepakanka: {produktas}")

def print_fridge_content():
    print("Šaldytuve šiuo metu yra: ")
    for produktas, kiekis in fridge_content.items():
        print(f"{produktas}: {kiekis}")

def check_recipe(receptas):
    reikalingi_produktai = dict(item.split(": ") for item in receptas.split(", "))
    truksta_produktu = {}

    for produktas, kiekis in reikalingi_produktai.items():
        kiekis = float(kiekis)
        if produktas in fridge_content and fridge_content[produktas] >= kiekis:
            continue
        else:
            truksta_kiekis = kiekis - fridge_content.get(produktas, 0)
            truksta_produktu[produktas] = truksta_kiekis

    if truksta_produktu:
        print("Receptui įgyvendinti trūksta šių produktų: ")
        for produktas, truksta_kiekis in truksta_produktu.items():
            print(f"{produktas}: {truksta_kiekis}")
    else:
        print("Visko turim, einam gaminti!")

def main():
    while True:
        print("\n[--GELTONAS ŠALDYTUVAS--]")
        print("\nPasitinkite veiksmą")
        print("1. Įdėti į šaldytuvą")
        print("2. Išimti iš šaldytuvo")
        print("3. Patikrinti ar yra šaldytuve")
        print("4. Peržiūrėti visą šaldytuvo turinį")
        print("5. Patikrinti ar užtenka produktų receptui")
        print("0. Išeiti iš programos")

        choice = input("Pasirinkite: ")

        if choice == "1":
            produktas = input("Pasirinkite produktą: ")
            kiekis = float(input("Įveskite kiekį: "))
            add_product(produktas, kiekis)
        elif choice == "2":
            produktas = input("Pasirinkite produktą: ")
            kiekis = float(input("Įveskite kiekį: "))
            remove_product(produktas, kiekis)
        elif choice == "3":
            produktas = input("Pasirinkite produktą: ")
            reikalingas_kiekis = float(input("Įveskite reikiamą kiekį: "))
            check_product_quantity(produktas, reikalingas_kiekis)
        elif choice == "5":
            receptas = input("Įveskite reikiamus produktus ir jų kiekius (pvz: Kiaušinis: 3, Sūris: 0.5 ir t.t.: ")
            check_recipe(receptas)
        elif choice == "4":
            print_fridge_content()
        elif choice == "0":
            print("Programos pabaiga.")
            break
        else:
            print("Netinkamas pasirinkimas. Bandykite dar kartą.")

if __name__ == "__main__":
    main()