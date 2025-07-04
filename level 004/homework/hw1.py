# მომხმარებელს შემოატანინე რიცხვი და მომხმარებლის შემოტანილ რიცხვამდე გამოიტანეთ ყველა რიცხვის კვადრატების ჯამი.
num = int(input("enter num"))
result = int(input("enter num"))
for number in range(num):
    result = number ** 2 + result
print(result)
