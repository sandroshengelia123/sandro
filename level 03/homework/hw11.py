text = input("შეიყვანეთ სტრინგი: ")
reversed_text = ""

# სტრინგის შებრუნება for loop-ით
for char in text:
    reversed_text = char + reversed_text

print("შებრუნებული ტექსტი:", reversed_text)

if text == reversed_text:
    print("ეს სტრინგი არის პალინდრომი")
else:
    print("ეს სტრინგი არ არის პალინდრომი")
