
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
