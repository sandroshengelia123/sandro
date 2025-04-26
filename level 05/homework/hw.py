# 1
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))

if num1 > num2:
    print(True)
elif num1 < num2:
    print(False)
else:
    print("Other")

# 2
my_name = "Giorgi"  # ჩასვი შენი სახელი აქ
input_name = input("შეიყვანე სახელი: ")
input_surname = input("შეიყვანე გვარი: ")

if input_name == my_name:
    print("we have same name")
else:
    print("we do not have same names")


# 3
my_name = "Giorgi"
my_age = 25  # ჩასვი შენი ასაკი აქ

if my_age > 18:
    if my_name == "Giorgi":
        print("we have same names and we are adults")
    else:
        print("we don't have same names but we are adults")
elif my_age < 18:
    print("we don't have same names and we are not adults")


# 4
fav_color = input("შეიყვანე შენი საყვარელი ფერი: ").lower()

if fav_color == "წითელი":
    print("red is favorite color")
elif fav_color == "ყვითელი":
    print("favorite color is yellow")
elif fav_color == "ლურჯი":
    print("favorite color is blue")
else:
    print("other color")

# 5
n = int(input("შეიყვანე რიცხვი: "))

# for loop
for i in range(1, n + 1):
    print(i)

# while loop
i = 1
while i <= n:
    print(i)
    i += 1

# 6
n = int(input("შეიყვანე ათზე მეტი რიცხვი: "))
total = 0

# for loop
for i in range(5, n + 1):
    total += i
print("ჯამი (for):", total)

# while loop
i = 5
total = 0
while i <= n:
    total += i
    i += 1
print("ჯამი (while):", total)


# 7
n = int(input("შეიყვანე 50-ზე მეტი რიცხვი: "))

# for loop
for i in range(1, n + 1, 5):
    print(i)

# while loop
i = 1
while i <= n:
    print(i)
    i += 5

