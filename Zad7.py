
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


