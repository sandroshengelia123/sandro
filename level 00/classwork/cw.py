# 1
# string - ტექსტური მონაცემია. გამოიყენება სიტყვების, წინადადებების და სიმბოლოების შესანახად. სტრინგი ჩერდება ბრჭყალებში " " ან ' '.
name = "Gio"
city = 'Tbilisi'


# intenger - მთელი რიცხვებია. არ შეიცავს ათწილადს.
age = 25
year = 2025

# float - ათწილადი რიცხვებია. შეიცავს წერტილს და წერტილის შემდეგ ციფრებს.
price = 12.99
height = 1.75

# boolean - ლოგიკური ტიპია და მხოლოდ ორი მნიშვნელობა აქვს: True ან False.
is_student = True
is_raining = False



# 2 
# ერთი და იგივე ცვლადში მონაცემთა სხვადასხვა ტიპების შენახვა
my_var = "Hello, world!"  # String
my_var = 42               # Integer
my_var = 3.14             # Float
my_var = False            # Boolean


# 3
# ინტეჯერის ფლოუტად გადაქცევა და დაბეჭდვა
number = 10          # Integer
number = float(number)  # გადაყვანა float ტიპად
print(number)        # შედეგი: 10.0

# 4
my_age = 25  # მაგალითად, შენი ასაკი
user_age = int(input("შეიყვანე შენი ასაკი: "))

difference = abs(my_age - user_age)
print("ჩვენს შორის ასაკობრივი განსხვავებაა:", difference, "წელი")

# 5
text = input("შეიყვანე ტექსტი: ")
repeat = int(input("რამდენჯერ დავბეჭდო ეს ტექსტი? "))

print(text * repeat)  # ან:
for i in range(repeat):
    print(text)


# 6
num1 = float(input("შეიყვანე float ტიპის რიცხვი: "))
num2 = int(input("შეიყვანე int ტიპის რიცხვი: "))

print("ჯამი:", num1 + num2)
print("სხვაობა:", num1 - num2)
print("ნამრავლი:", num1 * num2)
print("გაყოფა:", num1 / num2)
print("მთელი გაყოფა:", num1 // num2)
print("ხარისხი:", num1 ** num2)
print("ნაშთი:", num1 % num2)