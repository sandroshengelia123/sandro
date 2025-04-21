# 1) მომხმარებელს შემოატანინეთ რიცხვი და გამოიტანეთ ყველა რიცხვის კვადრატების ჯამი
number_input = int(input("შეიყვანეთ რიცხვი: "))

# კვადრატების ჯამი
sum_of_squares = 0
for i in range(1, number_input + 1):
    sum_of_squares += i ** 2

print(f"რიცხვების კვადრატების ჯამი 1-დან {number_input} ჩათვლით: {sum_of_squares}")


# 2) მომხმარებელს შემოატანინეთ რიცხვი და რიცხვიდან ამ რიცხვის კვადრატის ჩათვლით გამოიტანეთ ყველა რიცხვის ჯამი
number_input = int(input("შეიყვანეთ რიცხვი: "))

# ჯამი 1-დან რიცხვის კვადრატის ჩათვლით
sum_of_numbers = 0
for i in range(1, number_input ** 2 + 1):
    sum_of_numbers += i

print(f"რიცხვების ჯამი 1-დან {number_input} კვადრატის ჩათვლით: {sum_of_numbers}")


# 3) მომხმარებელს შემოატანინეთ სიტყვა და რიცხვი, შეინახეთ თითოეული ასოს რიცხვზე ნამრავლი
word_input = input("შეიყვანეთ სიტყვა: ")
number_input = int(input("შეიყვანეთ რიცხვი: "))

# თითოეული ასოს რიცხვზე ნამრავლი
new_string = ""
for char in word_input:
    new_string += char * number_input  # ასოს გამეორება რიცხვის მიხედვით

print(f"ნაწილი სიტყვა, რომელიც შედგება თითოეული ასოს ნამრავლით: {new_string}")


# 4) მომხმარებელს შემოატანინეთ სახელი მანამ სანამ თქვენს სახელს არ დაემთხვევა
my_name = "გიორგი"  # თქვენი სახელი

while True:
    name_input = input("შეიყვანეთ თქვენი სახელი: ")
    if name_input == my_name:
        print("დასწერით სწორად!")
        break  # წყვეტს ციკლს თუ სახელი სწორია
    else:
        print("არასწორი სახელი, სცადეთ კიდევ!")


# 5) მომხმარებელს შემოატანინეთ თქვენი საყვარელი ფერი მანამ სანამ არ გამოიცნობს
favorite_color = "ლურჯი"  # თქვენი საყვარელი ფერი

while True:
    color_input = input("რა არის ჩემი საყვარელი ფერი? ")
    if color_input.lower() == favorite_color.lower():
        print("კი! სწორია!")
        break  # წყვეტს ციკლს, თუ ფერი სწორია
    else:
        print("არასწორი ფერი, სცადეთ კიდევ!")


# 6) მომხმარებელს შემოატანინეთ რიცხვი და ყველა რიცხვი შეკრიბე
number_input = int(input("შეიყვანეთ რიცხვი: "))

sum_of_numbers = 0
i = 1
while i <= number_input:
    sum_of_numbers += i
    i += 1  # increment
print(f"ჯამი 1-დან {number_input} ჩათვლით: {sum_of_numbers}")


# 7) მომხმარებელს შემოატანინეთ პაროლი და ჰქონდეს სამი ცდა
correct_password = "mypassword"  # სწორი პაროლი
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password_input = input("შეიყვანეთ პაროლი: ")
    if password_input == correct_password:
        print("პაროლი სწორია!")
        break  # წყვეტს ციკლს, თუ პაროლი სწორი იყო
    else:
        attempts += 1
        print(f"არასწორი პაროლი. დარჩენილია {max_attempts - attempts} ცდა(ები).")
    
if attempts == max_attempts:
    print("სამწუხაროდ, სამჯერ მცდელობის შემდეგ პაროლი არასწორია.")


# 9) for loop და while loop-ი განსხვავება:
# for loop გამოიყენება როდესაც ვიცით რაოდენობა, რამდენჯერ უნდა განხორციელდეს ციკლი.
# while loop გამოიყენება მაშინ, როდესაც ჩვენ გვჭირდება იმ პონტში მუშაობა, სანამ გარკვეული პირობა არ შესრულდება.
# მაგალითად:
# for loop: 
# for i in range(5):   -> ვიმეორებთ ოპერაციას 5 ჯერ
# while loop:
# while condition:     -> ვიმეორებთ სანამ condition ჭეშმარიტია

# for loop-ი უფრო კავშირშია წვდომის რაოდენობასთან, მაშინ როდესაც while loop-ი უპირატესობას ანიჭებს პირობას.


