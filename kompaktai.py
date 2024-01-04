from datetime import datetime

class MuzikosKolekcija:
    def __init__(self):
        # Dainų kolekcija, kur raktas - daina, o reikšmė - trukmė
        self.dainu_kolekcija = {}

    def trukme_formatuoti(self, trukme):
        # Formatuoti trukmę į minutės:sekundės formatą
        minutes, seconds = divmod(int(trukme), 60)
        return f"{minutes:02d}:{seconds:02d}"

    def parse_trukme(self, trukme_text):
        # Konvertuoti trukmės tekstą į minutes su datetime moduliu
        try:
            trukme = datetime.strptime(trukme_text, "%M:%S")
            return trukme.minute * 60 + trukme.second
        except ValueError:
            print("Neteisingas trukmės formatas. Naudokite MM:SS formatą.")
            return None

    def prideti_daina(self, daina, trukme_text, kompaktas=None):
        # Tikrinama, ar kompaktas yra tuščias arba nurodytas
        if kompaktas is not None and kompaktas != '':
            # Tikrinama, ar kompaktas jau yra kolekcijoje
            if kompaktas not in self.dainu_kolekcija:
                naujas_kompaktas = input(f"Naujas kompaktas '{kompaktas}' nerastas. Įveskite naują kompaktą: ")
                self.dainu_kolekcija[naujas_kompaktas] = {}
            # Pridedama daina į kompaktą
            trukme = self.parse_trukme(trukme_text)
            if trukme is not None:
                self.dainu_kolekcija[kompaktas][daina] = trukme
        else:
            # Pridedama daina tiesiogiai į kolekciją
            trukme = self.parse_trukme(trukme_text)
            if trukme is not None:
                self.dainu_kolekcija[daina] = trukme

    def issimti_daina(self, daina):
        # Išimama daina iš kolekcijos
        for kompaktas, dainos in self.dainu_kolekcija.items():
            if daina in dainos:
                trukme = dainos.pop(daina)
                return trukme
        return None

    def patikrinti_kolekcija(self):
        # Spausdinama visos dainos ir jų trukmės kolekcijoje
        print("===[ Muzikos Kolekcija ]===")
        for kompaktas, dainos in self.dainu_kolekcija.items():
            print(f"{kompaktas}:")
            for daina, trukme in dainos.items():
                formatted_trukme = self.trukme_formatuoti(trukme)
                print(f"  {daina}: {formatted_trukme}")
        print("============================")

    def patikrinti_trukme(self):
        # Suskaičiuojama ir spausdinama, kiek laiko trunka visos dainos kolekcijoje
        bendra_trukme = sum(trukme for dainos in self.dainu_kolekcija.values() for trukme in dainos.values())
        formatted_bendra_trukme = self.trukme_formatuoti(bendra_trukme)
        print(f"Bendra dainų kolekcijos trukmė: {formatted_bendra_trukme}")


def rodyti_menu():
    print("\nPasirinkimai:")
    print("1. Pridėti dainą")
    print("2. Išimti dainą")
    print("3. Patikrinti kolekciją")
    print("4. Patikrinti trukmę")
    print("5. Baigti programą")


# Sukuriamas objektas MuzikosKolekcija
muzikos_kolekcija = MuzikosKolekcija()

# Vartotojo sąsaja
while True:
    rodyti_menu()
    pasirinkimas = input("Pasirinkite veiksmą (1-5): ")

    if pasirinkimas == '1':
        daina = input("Įveskite dainos pavadinimą: ")
        trukme_text = input("Įveskite dainos trukmę (sekundės): ")
        kompaktas = input("Įveskite kompaktą (jei nėra, palikite tuščią): ")
        muzikos_kolekcija.prideti_daina(daina, trukme_text, kompaktas)
    elif pasirinkimas == '2':
        daina = input("Įveskite dainos pavadinimą, kurią norite išimti: ")
        trukme = muzikos_kolekcija.issimti_daina(daina)
        if trukme is not None:
            formatted_trukme = muzikos_kolekcija.trukme_formatuoti(trukme)
            print(f"{daina} išimta iš kolekcijos. Trukmė: {formatted_trukme}")
        else:
            print(f"{daina} nerasta kolekcijoje.")
    elif pasirinkimas == '3':
        muzikos_kolekcija.patikrinti_kolekcija()
    elif pasirinkimas == '4':
        muzikos_kolekcija.patikrinti_trukme()
    elif pasirinkimas == '5':
        print("Programa baigta.")
        break
    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.")
