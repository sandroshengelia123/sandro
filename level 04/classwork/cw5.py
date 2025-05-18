correct_name = "Giorgi"      # ჩაანაცვლე შენს სახელად
correct_age = 25             # ჩაანაცვლე შენს ასაკად

name = ""
age = 0

while name != correct_name or age != correct_age:
    name = input("შეიყვანეთ სახელი: ")
    age = int(input("შეიყვანეთ ასაკი: "))

print("ყოჩაღ! სახელი და ასაკი სწორია.")