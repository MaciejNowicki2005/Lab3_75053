# ZADANIE 4

iloscOsob = int(input("Ilu was było?"))
osoba = [iloscOsob]
iloscDan = int(input("Ilu potraw zamowiono?"))
dania = []
kosztRachunku = [0] * iloscOsob
suma = 0
i = 0

while i < iloscOsob:
    try:
        ileZamowiono = int(input(f"Osoba {i + 1}, ile zamówiła dań? :"))
    except ValueError:
        print("Blad danych.")
        continue

    if ileZamowiono < 0 or len(dania) + ileZamowiono > iloscDan:
        print("Błędna liczba dań!")
        continue

    for j in range(ileZamowiono):
        while True:
            try:
                cena = float(input(f"Koszt dania {j + 1} osoby {i + 1}: "))
                if cena < 0:
                    print("Podaj prawdziwą cenę!")
                    continue
                kosztRachunku[i] += cena
                dania.append(cena)
                break
            except ValueError:
                print("Podaj prawdziwą cenę!")

    suma += kosztRachunku[i]
    i += 1

k = 0
for k in range(iloscOsob):
    print(f"Osoba {k + 1} musi zapłacić: {kosztRachunku[k]:.2f} zł")

if iloscDan > 0:
    print(f"Suma zamówienia wynosiła: {suma} zł, co daje nam średnio {suma / iloscDan} zł za danie")
else:
    print(f"Suma zamówienia wynosiła: {suma} zł")

if len(dania) != iloscDan:
    print("Uwaga: liczba wprowadzonych dań nie zgadza się z deklarowaną!")





