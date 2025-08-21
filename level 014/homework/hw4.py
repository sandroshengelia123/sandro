# შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ სტრინგს დაფარავს *-ით
def username(userword):
    result = ""
    for i in userword:
        result += "*"
    return result
print(username("heelo"))