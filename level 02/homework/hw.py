# 1
# AND ოპერატორი
print(True and True)     # True  - ორივე მხარე True, შედეგი True
print(True and False)    # False - ერთი მხარე False, შედეგი False
print(False and True)    # False - ერთი მხარე False, შედეგი False
print(False and False)   # False - ორივე მხარე False, შედეგი False

# OR ოპერატორი
print(True or True)      # True  - ერთი მხარე True, შედეგი True
print(True or False)     # True  - ერთი მხარე True, შედეგი True
print(False or True)     # True  - ერთი მხარე True, შედეგი True
print(False or False)    # False - ორივე მხარე False, შედეგი False


# 2
# AND და OR ოპერატორების უპირატესობა
result = True or False and False   # OR ოპერატორი გამოიყენება ბოლო რიგში, რადგან AND უფრო მაღალი პრიორიტეტი აქვს.
print(result)  # True, რადგან False and False = False, შემდეგ True or False = True

result = (True or False) and False  # აქ parentheses-მა შეცვალა პრიორიტეტი, და წინა შედეგი გაითვალისწინეთ
print(result)  # False, რადგან True or False = True, შემდეგ True and False = False


# 3
# გადავიკვლიეთ თითოეული ოპერაცია
result = True or True and False or True and False
print(result)


# 4
# 4) მომხმარებელს შემოატანინეთ სახელი და შეამოწმე, მონაცემთა ტიპი თუ არის სტრინგი
name_input = input("შეიყვანეთ თქვენი სახელი: ")
if isinstance(name_input, str):  # ვამოწმებთ, რომ ცვლადი არის სტრინგი
    print("თქვენი სახელი არის სტრინგი.")
else:
    print("თქვენი სახელი არ არის სტრინგი.")


# 5
# 5) მომხმარებელს შემოატანინეთ სახელი. გამრავლება 5-ჯერ და შეამოწმე, თუ ეს სტრინგი თუ ინტეჯერი არის.
name_input = input("შეიყვანეთ თქვენი სახელი: ")
multiplied_name = name_input * 5  # სახელი 5-ჯერ გაიმეორება

# შეამოწმოთ, თუ ეს სტრინგი ან ინტეჯერი არის
if isinstance(multiplied_name, str) or isinstance(multiplied_name, int):
    print(f"გამრავლებული სახელი: {multiplied_name}")
    print(f"მონაცემთა ტიპი: {type(multiplied_name)}")
else:
    print("შედეგი არაა სტრინგი ან ინტეჯერი.")


# 6 მომხმარებელს შემოატანინეთ ასაკი და დაპრინტე მონაცემთა ტიპი
age_input = input("შეიყვანეთ თქვენი ასაკი: ")
age = int(age_input)  # გადაყავს სტრინგი ინტეჯერში
print(f"თქვენი ასაკი არის: {age}")
print(f"მონაცემთა ტიპი: {type(age)}")
