#  შექმენით ფუნქცია სადაც მომხმარებლის შემოტანილი რიცხვის გამყოფების ჯამს დაგვიბრუნებს. 
num = int(input("enter num"))
def i (num):
    b = 0
    for i in range(1, num):
        if num % i == 0:
            b += i
    return(b)
print(i(num))