# შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ სტრინგში ლუწ ინდექსზე მდომ სიმბოლოებს დაგვიბრუნებს.
def username(user):
    result = ""
    for i in range(len(user)):
        if i % 2 == 0:
            result += user[i]
    return result
print(username("hallo"))