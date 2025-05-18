correct_password = "12445"
attempts = 0

while attempts < 3:
    password = input("შეიყვანე პაროლი:")
    if password == correct_password:
        print ("მიღებულია!")
        break
    else:
        print("არასწორია.")
        attempts == 1

if attempts == 3:
    print("მოგვიანებით ცადე!")