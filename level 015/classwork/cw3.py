# შექმენი ფუნქცია როომელსაც გადაეცემა სტრინგი --> fortoxali,თქვენი დავალებაა დააბრუნოთ თითოეული ასოს ინდექსი სიის სახით (არ გამოიყენოთ len ფუნქცია)
def user(username):
    result = []
    for i in username:
       result.append (username.index(i))
    return result
print(user("fortoxali"))