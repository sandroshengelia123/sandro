# მომხმარებელს შემოატანინე რიცხვი,for loop ის გამოყენებით გამოიტანე თითოეული რიცხვი ერთიდან ამ რიცხვამდე,იგივე გააკეთეთ While loop-ით
num = int(input("enter num"))
for i in range(num):
    print(i)


num = int(input("enter num"))
result = 0
while result < num:
    print(result)
    result += 1