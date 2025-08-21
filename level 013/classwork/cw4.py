# 4) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია სადაც იქნება სხვადასხვა ტიპის მონაცემი. გაიგეთ ამ სიაში რიცხვების ჯამი
def sum_number(user_list):
    sum = 0
    for i in user_list:
        if type(i) == int or type(i) == float:
            sum += i
    return sum
print(sum_number([12, True, "25", 20.9]))