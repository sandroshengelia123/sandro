# 1
# ცვლადების შექმნა snake_case სტილით
user_name = "Gio"
user_age = 25
user_city = "Tbilisi"

# გამოსატანი ტექსტი
print("სახელი:", user_name)
print("ასაკი:", user_age)
print("ქალაქი:", user_city)


# 2
# სამი ცვლადის შექმნა snake_case სტილით
book_title = "1984"           # ეს ცვლადი ინახავს წიგნის სახელს
author_name = "George Orwell" # ეს ცვლადი ინახავს ავტორის სახელს
publication_year = 1949       # ეს ცვლადი ინახავს გამოსვლის წელს

# მონაცემების დაბეჭდვა
print(book_title)
print(author_name)
print(publication_year)

# 3
# კონკატენაცია ნიშნავს სტრინგების შეერთებას
# როდესაც ორ ან მეტ ტექსტს (სტრინგს) ვაერთებთ ერთად, ამას ქვია კონკატენაცია

# სტრინგებს ვაერთებთ + ნიშნით
first_name = "Luka"
last_name = "Beridze"

# ვაერთებთ ორ სტრინგს
full_name = first_name + " " + last_name

print(full_name)  # შედეგი: Luka Beridze

# თუ სტრინგს ვაერთებთ სხვა ტიპის მონაცემს (მაგ: int ან float), საჭიროა მისი str()-ით გარდაქმნა

age = 20
text = "მე ვარ " + str(age) + " წლის"

print(text)  # შედეგი: მე ვარ 20 წლის

name = "Nika"
age = 18

# f-string სტრინგების გასაერთიანებლად
print(f"{name} არის {age} წლის")  # შედეგი: Nika არის 18 წლის

# 5
# მომხმარებლისგან ვიღებთ მონაცემებს input() ფუნქციით
# რიცხვები ვაქცევთ int ტიპად, სტრინგები 그대로 ინახება

car_name = input("შეიყვანე ავტომობილის სახელი: ")
car_color = input("შეიყვანე ავტომობილის ფერი: ")
car_price = int(input("შეიყვანე ავტომობილის ფასი (რიცხვით): "))
car_year = int(input("შეიყვანე ავტომობილის გამოშვების წელი (რიცხვით): "))

# ვაკეთებთ კონკატენაციას ანუ სტრინგების შეერთებას
# რადგან გვაქვს რიცხვები, საჭიროა str() ფუნქციით გარდავქმნათ სტრინგად

car_info = "ავტომობილის დასახელებაა " + car_name + ", მისი ფერია " + car_color + ", ფასი არის " + str(car_price) + " ლარი და გამოშვების თარიღია " + str(car_year) + " წელი."

# ვბეჭდავთ საბოლოო წინადადებას
print(car_info)

# 6
# ცვლადი 1 - Integer (მთელი რიცხვი)
user_age = 25

# ცვლადი 2 - String (ტექსტი)
user_name = "Nino"

# ცვლადი 3 - Float (ათწილადი)
user_height = 1.68

# ცვლადი 4 - Boolean (True/False)
is_student = True


print("ასაკი:", user_age)
print("სახელი:", user_name)
print("სიმაღლე:", user_height)
print("სტუდენტია:", is_student)


# 7
# მომხმარებლისგან მონაცემების მიღება input() ფუნქციით
living_place = input("შეიყვანე შენი საცხოვრებელი ადგილი: ")
favorite_animal = input("შეიყვანე შენი საყვარელი ცხოველი: ")

# მიღებული მონაცემების დაბეჭდვა
print("შენ ცხოვრობ:", living_place)
print("შენს საყვარელ ცხოველს ეწოდება:", favorite_animal)

# 8
# 1. ვქმნით ცვლადს და ვანიჭებთ მთელ რიცხვს (integer)
number_int = 100

# 2. ვაქცევთ მას სტრინგად შესაბამისი ფუნქციით (str())
number_str = str(number_int)

# 3. ვქმნით მეორე ცვლადს, სადაც რიცხვი შენახულია როგორც სტრინგი
text_number = "250"

# 4. ამ სტრინგ ტიპის რიცხვს ვაქცევთ ინტეჯერად (int())
converted_number = int(text_number)

# 5. დავბეჭდოთ რომ ყველაფერი სწორად იმუშავა
print("სტრინგად ქცეული რიცხვი:", number_str)
print("ინტეჯერად ქცეული სტრინგი:", converted_number)


# 9
# მომხმარებლისგან ორი რიცხვის მიღება
num1 = float(input("შეიყვანე პირველი რიცხვი: "))
num2 = float(input("შეიყვანე მეორე რიცხვი: "))

# მათემატიკური ოპერაციები
sum_result = num1 + num2         # ჯამი
difference = num1 - num2         # სხვაობა
product = num1 * num2            # ნამრავლი
division = num1 / num2           # გაყოფა
integer_division = num1 // num2  # მთლიანი გაყოფა (გამორიცხავს ათწილადებს)
power = num1 ** num2             # ამაღლება ძალზე
modulus = num1 % num2            # ნაშთი

# შედეგების დაბეჭდვა
print("ჯამი:", sum_result)
print("სხვაობა:", difference)
print("ნამრავლი:", product)
print("გაყოფა:", division)
print("მთელი გაყოფა:", integer_division)
print("ხარისხი:", power)
print("ნაშთი:", modulus)

# ---------------

# % (modulus) - ნაშთი (modulus) არის ოპერაცია, რომელიც გვაძლევს რიცხვებს შორის ხანგრძლივი გაყოფის ნაშთს
# მაგალითად, 10 % 3 = 1, რადგან 10 ნაწილდება 3-ზე 3-ჯერ, ხოლო ნაშთი არის 1.