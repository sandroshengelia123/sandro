# შექმენი ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია,თქვენი დავალებაა დააბრუნოთ ახალი სია სადაც გექნებათ მხოლოდ ლუწი რიცხვები
def user(username):
    result = []
    for i in username:
        if i % 2 == 0:
            result.append(i)
    return result
print(user([2, 10, 15]))