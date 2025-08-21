# შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის სახელი და ასაკი. შეამოწმეთ თუ ასაკი მეტი არის 18-ზე და მისი სახელი არის თქვენი სახელის ტოლი მაშინ დააბრუნოს თქვენ წარმატებით აიღეთ მართვის მოწმობა. სხვა დანარჩენ შემთხვევაში რომ ჩაიჭრნენ
def name_age(username, age):
    if age > 18 and username == "sandro":
        return "tqven warmatebit aiget martvis mowmoba"
    else:
        return "chaiwras"
name_age("hello", 17)
print(name_age("hello", 17))