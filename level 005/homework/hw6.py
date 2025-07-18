# მარებლის შემოტანილ რიცხვამდე ყველა რიცხვის მომხმარებელს შემოატანინე ათზე მაღალი რიცხვი,for loop ის გამოყენებით იპოვეთ 5 დან მომხჯამი,იგივე გააკეთეთ while loop ითაც
num = input("enter num")
result = 0
if num > 10:
    for i in range(5, num):
        result += i
        print(result)
else:
    print("10 ze magali ricxvi")


num = input("enter num")
result = 0
if num > 10:
    i = 5
    while i < num:
        result += i
        print(result)
        i += 1
else:
    print("10 tze naklebi ricxvi")