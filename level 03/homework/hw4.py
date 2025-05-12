end = int(input("შეიყვანეთ რიცხვი: "))

for i in range(1, end + 1):
    if i == 5:
        continue  # გამოტოვებს 5-ს
    print(i)
