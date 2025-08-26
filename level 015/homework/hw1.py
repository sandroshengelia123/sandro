# შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი,შენი დავალებაა ამ სტრინგიდან ამოშალო კენტ იდექსზე მდგომი ასოები და დააბრუნო სტრინგი მათ გარეშე
def username(user):
    result = ""
    for i in range(len(user)):
        if i % 2 == 0:
            result += user[i]
    return result
print(username("30"))