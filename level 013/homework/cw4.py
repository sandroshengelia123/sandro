#  შექმენით ფუნქცია რომელიც მომხმარებელს შემოატანინებს სიტყვას მანამ სანამ არ შემოიტანს 'საკმარისია'ს. ეს შემოტანილი სიტყვები დაამატეთ სიაში და გაფილტრეთ. სიაში უნდა იყოს ისეთი სიტყვები რომლის სიგრძეც არ აღემატება 5-ს და ურევია რიცხვები.
def username():
    name = input("enter ")
    user_list = []
    while name != "sakmarisia":
        if len(name)< 5:
          for i in name:
             if i in "0123456789":
                user_list.append(name)
                break
        name = input("enter")
    return user_list
print(username())