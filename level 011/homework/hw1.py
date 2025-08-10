#  მომხმარებელს შეეკითხეთ ორი რიცხვი შემდეგ კი შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ ამ ორ რიცხვს ხოლო ფუნქცია დააბრუნებს ამ ორი რიცხვის ჯამს, ასევე გააკეთე ასეთი 4 ფუნქცია სხვადასხვა მათემატიკური მოქმედებებისთვის, გამოიყენეთ პარამეტრები და არგუმენტად გადაეცით მომხარებლის შემოტანილი რიცხვები
num = int(input("enter num"))
num2 = int(input("enter num"))
def i (num, num2):
    return(num + num2)
print(i(num, num2))
def a (num, num2):
    return(num - num2)
print(a(num, num2))
def c (num, num2):
    return(num * num2)
print(c(num, num2))
def b (num, num2):
    return(num / num2)
print(b(num, num2))