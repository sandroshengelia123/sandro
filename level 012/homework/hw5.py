# შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებს სიტყვას და მანამ უნდა შემოატანინოთ სანამ არ შემოიტანს “საკმარისია”. ყველა შემოტანილი სიტყვა დაამატეთ ახალ სიაში და ეს სია დააბრუნეთ.
def i ():
    text = input("enter text")
    user_list = []
    while text != "sakmarisia":
        user_list.append(text)
        text = input("enter text")
    return(user_list)
print(i())