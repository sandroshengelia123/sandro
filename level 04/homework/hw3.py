word = input("შეიყვანეთ სიტყვა: ")
multiplier = int(input("შეიყვანეთ რიცხვი: "))
result = ""

for letter in word:
    result += letter * multiplier

print(f"შედეგი: {result}")
