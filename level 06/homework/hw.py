# 1
# String (ტექსტი) - მონაცემის ტიპი ტექსტის შესანახად
name = "Nino"

# Integer (მთელი რიცხვი)
age = 25

# Float (ათწილადი რიცხვი)
weight = 65.5

# Boolean (ლოგიკური მნიშვნელობა: True ან False)
is_adult = True

# List (სია) - ელემენტების კოლექცია
fruits = ["apple", "banana", "cherry"]

# Tuple (ტუპლი) - უცვლელი ელემენტების კოლექცია
colors = ("red", "green", "blue")

# Dictionary (ლექსიკონი) - key:value წყვილებით მონაცემთა შენახვა
person = {"name": "Nino", "age": 25}

# 2
my_string = "30"
my_int = 20

# int -> str
converted_str = str(my_int)

# str -> int
converted_int = int(my_string)

print(converted_str)
print(converted_int)

# 3
name = input("შეიყვანე სახელი: ")
surname = input("შეიყვანე გვარი: ")
age = int(input("შეიყვანე ასაკი: "))
weight = float(input("შეიყვანე წონა: "))

print(f"{name} {surname} არის {age} წლის და იწონის {weight} კგ.")


# 4
a = 10
b = 5

print(a + b)  # + შეკრება
print(a - b)  # - გამოკლება
print(a * b)  # * გამრავლება
print(a / b)  # / გაყოფა
print(a % b)  # % ნაშთი
print(a ** b) # ** ხარისხში აყვანა
print(a // b) # // მთლიანი გაყოფა

print(a > b)   # მეტობა
print(a < b)   # ნაკლებობა
print(a == b)  # ტოლი
print(a != b)  # არ არის ტოლი
print(a >= b)  # მეტია ან ტოლი
print(a <= b)  # ნაკლებია ან ტოლი


# 5
# AND ოპერატორი აბრუნებს True-ს მხოლოდ მაშინ, როცა ორივე პირობაა True
x = 10
print(x > 5 and x < 20)  # True

# OR ოპერატორი აბრუნებს True-ს თუნდაც ერთი პირობა მაინც True იყოს
y = 3
print(y > 5 or y < 10)   # True


# 6
# for loop
for i in range(1, 101, 10):
    print(i)

# while loop
i = 1
while i <= 100:
    print(i)
    i += 10


# 7
# for loop
total = 0
for i in range(1, 21):
    total += i
print("ჯამი (for):", total)

# while loop
i = 1
total = 0
while i <= 20:
    total += i
    i += 1
print("ჯამი (while):", total)


# 8
age = int(input("შეიყვანე ასაკი: "))

if age > 30:
    print("ზრდასრული ხარ")
elif age == 30:
    print("შენ ხარ 30 წლის")
else:
    print("კარგი ასაკი გაქვს")
