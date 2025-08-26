# შექმენი ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა სიიდან ამოშალოთ მხოლოდ ის სიტყვები რომლის სიგრძეც ნაკლებია 5 ზე
def user(username):
    result = []
    for i in username:
        if len(i) < 5:
            result += i
    return result
print(user(["25", "30", "50"]))