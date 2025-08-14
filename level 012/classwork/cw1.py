#  შექმენით ფუნქცია, სადაც მოხმარებელს შემოატანინებთ რიცხვს და ამ რიცხვის გამყოფებს დააბრუნებს სიაში.
def gamyofilebi(num):
    divs = []
    for i in range (1, num + 1):
        if num % 1 == 0:
            divs.append(i)
    return divs
num = int(input("enter num"))
print(gamyofilebi(num))