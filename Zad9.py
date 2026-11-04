
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
