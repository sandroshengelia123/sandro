my_name = "sandro"

while True:
    my_name =input("შეიყვანე ჩემი სახელი:")
    if my_name.lower() == my_name:
        print("სწორია")
        break
    else:
        print("არასწორია,თავიდან სცადე")