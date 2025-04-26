# 1
# String (ტექსტი)
my_string = "Hello, World!"

# Integer (მთელი რიცხვი)
my_integer = 42

# Float (ათწილადი რიცხვი)
my_float = 3.14

# Boolean (ლოგიკური მნიშვნელობა)
my_boolean = True



# 2
# ცვლადები
my_string = "123"       # string ტიპის მნიშვნელობა
my_integer = 456        # integer ტიპის მნიშვნელობა

# გარდაქმნები
converted_to_int = int(my_string)     # string -> int
converted_to_str = str(my_integer)    # int -> string

# შედეგის დაბეჭდვა
print("სტრინგიდან ინტეჯერად:", converted_to_int, type(converted_to_int))
print("ინტეჯერიდან სტრინგად:", converted_to_str, type(converted_to_str))



# 3
# მონაცემების მიღება
name = input("შეიყვანე შენი სახელი: ")                  # String
age = int(input("შეიყვანე შენი ასაკი: "))               # Integer
height = float(input("შეიყვანე შენი სიმაღლე (მაგ: 1.75): "))  # Float

# შედეგის ჩვენება
print("სახელი:", name)
print("ასაკი:", age, "ტიპი:", type(age))
print("სიმაღლე:", height, "ტიპი:", type(height))


# 4
# ცვლადების შექმნა
num1 = 17
num2 = 5

# ნაშთი (modulo)
remainder = num1 % num2

# რამდენჯერ მოთავსდება num2 ცვლადი num1-ში (მთლიანი გაყოფა)
quotient = num1 // num2

# შედეგების დაბეჭდვა
print("ნაშთი:", remainder)
print("მთლიანი რაოდენობა რამდენჯერ მოთავსდება:", quotient)
