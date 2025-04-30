# 1) გადმოიტანეთ სიის პირველი და ბოლო ელემენტი
names = ["george", "davit", "mariam", "nika", "sandro"]
print(names[0]) # first element
print(names[-1]) # last element

# 2) კომენტარებიT უარყოფიტი ინდექსები
names = ["sandro", "eka", "sesily", "george", "andria",]
# -5        -4       -3     -2         -1

# 3 for loop-ით გადმოიტანეთ თითოეული ელემენტი
names = ["nino", "anastasia", "andria", "tamari",]
for name in names:
    print(name)

# 4) სტრინგიდან თოთოეული ასოს გამოყვანა
text = "hello"
for letter in text:
    print(letter)

# 5) slicing 2-დან  7 ინდექსამდე
names = ["eka", "snadro", "luka", "vaxo", "zura", "irakli", "elene",]
print(names[2:8]) # 2 ინდექსიდან 7-მდე (8-გამორიცხულია)

# 6) სტრინგის ბოლო 8 ასოს გამოყვანა
word = "აქსიომა"
print(word[-8]) # ბოლო 8 ასო

# 7) სიის ყველა ელემნტის ჩანაცვლება
fruits = ["banana", "apple", "mango", "pear"]
countries = ["საქართველო", "საფრანგეთი", "იტალია", "ესპანეთი"]
fruits = countries
print(fruits)

# 8) სტრინგის ბოლო ინდექსის შეცვლა
text = "fruits"
# text[-1] = "k"  # ეს კოდი გამოიწვევს შეცდომას
# კომენტარი: სტრინგები Python-ში უცვლადია (immutable), ვერ ვცვლით ცალკეულ სიმბოლოს უშუალოდ.

# 9) "kurdgelia" სტრინგიდან "gela"
word = "kurdgelia"
print(word[4:8])  # ინდექსები 4-დან 7-მდე

# 10) სიის ელემენტების ჯამი
numbers = [10, 5, 20, 40]
print(sum(numbers))