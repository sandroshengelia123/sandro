# შექმენით ფუნქცია, რომელიც მომხმარებლის შემოტანილ float ტიპის მოცანემს გახლიჩავს. შედეგი ასე რომ იყოს :  19.27 => 19 + 0.27 
def username(userword):
    return str(int(userword)) + "+" + str(userword - int(userword))
print(username(30.5))