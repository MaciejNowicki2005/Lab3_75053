
# ZADANIE 1
import time
paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Zostało {paliwo} paliwa")
    czas = czas + 1
    time.sleep(1)
    paliwo = paliwo - paliwo_zużyte_na_s

print(f"Koniec paliwa!!! Czas lotu {czas}")


# ZADANIE 2

liczba = 2
ile = 0

while ile < 10:
    dzielnik = 2

    while dzielnik < liczba:
        if liczba % dzielnik == 0:
            break
        dzielnik += 1

    if dzielnik == liczba:
        if ile > 0:
            print(",", end="")
        print(liczba, end="")
        ile += 1

    liczba += 1


# ZADANIE 3
ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]

print(len(ulice))

for i in range(len(ulice)):
    for j in range(5):
        for k in range(10):
            print(f"{ulice[i]}, nr.{j+1}, mieszkanie{k+1}")


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





# ZADANIE 5
liczbaStartowa = 80

for l in range(liczbaStartowa,-1,-4):
    print(f"Liczba: {l}")

# ZADANIE 6

while True:
    lCalkowita = int(input("Podaj liczbę całkowitą nieujemną: "))

    if lCalkowita >= 0:
        continue

    if lCalkowita < 0:
        print("Błędna liczba, kończymy!")
        break


# ZADANIE 7A
n = int(input("Ile studentów: "))

if n > 0:
    studenci = []
    iterator = 0
    sumaPkt = 0

    while iterator < n:
        punkty = int(input(f"Ilość punktów dla studenta {iterator+1}: "))

        if punkty > 100 or punkty < 0:
            print("Błędna wartość!")
            continue

        studenci.append(punkty)
        sumaPkt += punkty
        iterator += 1

    srednia = sumaPkt / n
    print(f"Średnia liczba punktów: {srednia}")
else:
    print("Brak studentów :(")


# ZADANIE 7B
n = int(input("Ile studentów: "))

studenci = []
iterator = 0
sumaPkt = 0

while True:
    if iterator >= n:
        break

    punkty = int(input(f"Ilość punktów dla studenta {iterator+1}: "))

    if punkty > 100 or punkty < 0:
        print("Błędna wartość!")
        continue

    studenci.append(punkty)
    sumaPkt += punkty
    iterator += 1

if n > 0:
    srednia = sumaPkt / n
    print(f"Średnia liczba punktów: {srednia}")
else:
    print("Brak studentów :(")


# ZADANIE 8
tekst = "Python jest super"

print(f"Znak 0: {tekst[0]}")
print(f"Znak ostatni: {tekst[len(tekst)-1]}")
print(f"Znak co drugi: {tekst[0:len(tekst):2]}")
print(f"Znak co trzeci: {tekst[1:len(tekst):3]}")
print(f"Znak od 10 do przedostatniego: {tekst[10:len(tekst)]}")
print(f"Znak od ostatniego do pierwszego: {tekst[::-1]}")


# ZADANIE 9A
imie = input("Podaj swoje imię: ")
print(f"Witaj, {imie}")


# ZADANIE 9B
try:
    wiek = int(input("Podaj swój wiek: "))
    print(f"Twój wiek to: {wiek}")
except ValueError:
    print("Niepoprawne dane.")


# ZADANIE 9C
inicjaly = ""

imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")

if imie and nazwisko:
    inicjaly += imie[0] + nazwisko[0]
    print(f"Inicjały {imie} {nazwisko} to: {inicjaly.upper()}")
else:
    print("Nie podano imienia lub nazwiska.")


# ZADANIE 9D
lancuch = input("Podaj dowolny łańcuch znaków: ")

for i in range(5):
    print(lancuch)


# ZADANIE 9E
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")

laczony = lancuch1 + lancuch2
print(f"Połączone łańcuchy to: {laczony}")


# ZADANIE 9F
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")

laczony = lancuch1[:len(lancuch1)//2] + lancuch2[:len(lancuch2)//2]
print(f"Połączone połówki łańcuchów to: {laczony}")
