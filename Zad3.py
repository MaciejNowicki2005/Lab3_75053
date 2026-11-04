
# ZADANIE 3
ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]

print(len(ulice))

for i in range(len(ulice)):
    for j in range(5):
        for k in range(10):
            print(f"{ulice[i]}, nr.{j+1}, mieszkanie{k+1}")


