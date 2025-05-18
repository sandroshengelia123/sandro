num = int(input("შეიყვანეთ რიცხვი: "))
total = 0

for i in range(num, num ** 2 + 1):
    total += i

print(f"{num}-დან {num**2}-მდე რიცხვების ჯამი არის: {total}")
