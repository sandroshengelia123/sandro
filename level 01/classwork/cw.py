# 1
# ხუთი ცვლადის შექმნა snake_case სტილით

user_name = "Luka"
user_age = 22
favorite_food = "ხაჭაპური"
hobby = "კალათბურთი"
is_student = True

# ხუთივე ცვლადის დაბეჭდვა
print(user_name)
print(user_age)
print(favorite_food)
print(hobby)
print(is_student)


# 2
# სამი ცვლადი, სახელით ძალიან ჰგავს ერთმანეთს, მაგრამ მაინც განსხვავდება

name = "Gio"        # პატარა ასოებით
Name = "Nino"       # დიდი ასო N-ით
name_ = "Lasha"     # ბოლოს ქვედა ტირე

# სამივე ცვლადის დაბეჭდვა
print(name)
print(Name)
print(name_)


# 3
# მომხმარებლისგან მონაცემების მიღება
first_name = input("შეიყვანე შენი სახელი: ")
last_name = input("შეიყვანე შენი გვარი: ")
age = input("შეიყვანე შენი ასაკი: ")
height = input("შეიყვანე შენი სიმაღლე: ")

# კონკატინაცია (გაერთიანება) space-ებით გამოყოფით
user_info = first_name + " " + last_name + " " + age + " " + height

# შედეგის დაბეჭდვა
print(user_info)


age = int(input("შეიყვანე ასაკი: "))
height = float(input("შეიყვანე სიმაღლე: "))

# და შემდეგ str()-ით გადავაქციოთ სტრინგად:
user_info = first_name + " " + last_name + " " + str(age) + " " + str(height)
