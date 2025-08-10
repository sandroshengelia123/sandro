#  შექმენით ფუნქცია რომელსაც გადაეცემა სია, ამ სიში უნდა იყოს ყველა ტიპის მონაცემი. დააბრუნეთ ინტეჯეტ ტიპის ელემენტები ახალ სიაში.
num = ["40", 19.0, 60, True, "50", False]
user_list = []
for i in num:
    if type(i) == int:
        user_list.append(i)
print(user_list)