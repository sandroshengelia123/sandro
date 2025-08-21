# შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ რიცხვის ჩათვლით გამოგვიტანს ყველა მარტივი რიცხვის ნამრავლს.
def username(user):
    result = 1
    for i in range(2, user):
        for a in range(2, i):
            if i % a == 0:
                break
        else:
            result = i * result
    return result
print(username(50))