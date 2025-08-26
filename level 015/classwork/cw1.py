# შექმენი ფუნქცია,რომელსაც გადაეცემა სტრინგი --> aleqsandre , თქვენი დავალებაა დააბრუნოთ კენტ ინდექსზე მდგომი ასოები
def username(user):
    result = ""
    for i in range(len(user)):
        if i % 2 == 1:
            result += user[i]
    return result
print(username("aleqsandre"))