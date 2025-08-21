#  შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ რიცხვს დაშლის მამრავლებად. მაგალითად ასე => თუ შემოიტანა რიცხვი 1980 მაშინ შედეგი იყოს 1000 + 900 + 80 (მარტო 1980-ზე არ განიხილოთ ეგ, მაგალითად მოვიყვანე რომ მიხვდეთ ! )
def username(user):
    result = ""
    sigrdzes = len (str(user)) -1
    for i in str(user):
        if i != "0":
            result += i + sigrdzes * "0" + "+"
        sigrdzes -= 1
    return result [: -1]
print(username(1890))