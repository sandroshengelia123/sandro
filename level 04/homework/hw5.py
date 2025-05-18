favorite_color = "blue"

while True:
    color = input("მოიტანე ჩემი საყვარელი ფერი:")
    if color.lower() == favorite_color:
        print("სწორია!")
        break
    else:
        print("არასწორია, თავიდან სცადე")