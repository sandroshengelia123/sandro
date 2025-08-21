# შექმენით ფუნქცია რომელიც მომხმარებელის შემოატანილ რიცხვის ფაქტორიალს დააბრუნებს.
def username(user):
    result = 1
    for i in range(2, user):
        result *= i 
    return result
print(username(40))