# მომხმარებელს შემოატანინე რიცხვი და მომხმარებლის შემოტანილი რიცხვიდან ამ რიცხვის კვადრატის ჩათვლით გამოიტანეთ ყველა რიცხვის ჯამი
num = int(input("enter num"))
result = 0
for number in range(num, num ** 2):
    result = num  + result
print(result)