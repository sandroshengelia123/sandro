# შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი --> "hidroeleqtrosadguri" ,თქვენი დავალებაა ამოშალოთ ამ სტრინგიდან მხოლოდ ხმოვნები და დააბრუნოთ ეს სტრინგი ხმოვნების გარეშე
def username(user):
    result = ""
    for i in user:
        if i != "e" and i != "o" and i != "a" and i != "u" and i != "i":
            result += i
    return result
print(username("hidroeleqtrosadguri"))