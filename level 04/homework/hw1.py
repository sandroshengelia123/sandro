num = int(input("შეიყვანეთ რიცხვი: "))
sum_of_squares = 0

for i in range(1, num + 1):
    sum_of_squares += i ** 2

print(f"{num}-მდე რიცხვების კვადრატების ჯამი არის: {sum_of_squares}")
