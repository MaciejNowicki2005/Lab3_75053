#ZADANIE 2

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

