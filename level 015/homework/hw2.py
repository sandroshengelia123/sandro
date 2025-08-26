# შექმენი ფუნქცია რომელსაც დაგაეცემა სია,შენი დავალებაა ამ სიიდან ამოშალო კენტ ინდექსზე მდგომი მხოლოდ კენტი რიცხვები და დაამატო ეს რიცხვები ახალ სიაში
def user_list(user):
    user_list1= []
    for i in user:
        if i % 2 == 1 and user.index(i ) % 2 == 1:
            user_list1.append(i)
    return user_list1
print(user_list([3, 40, 6, 7, 10]))
            