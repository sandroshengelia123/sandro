# მომხმარებელს შემოატანინე 50 ზე მაღალი რიცხვი for loop გამოყენებით ერთიდან მომხმარებლის შემოტანილ რიცხვამდეე დაბეჭდეთ ყველა რიცხვი 5 step ის გამოყენებით,იგივე გაააკეთეთ while loop ითაც
num = int(input("enter num"))
if num > 50:
    for i in range(1, num, 5):
        print(i)


num = int(input("enter num"))
if num > 50:
    
    i = 1
    while i < num:
        i += 1
        print(i)