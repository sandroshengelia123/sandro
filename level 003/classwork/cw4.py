# 4) მომხმარებელს შემოატანინე ორი სტრინგი და for loop-ის საშუალებით დაითვალე  ორივეში სიმბოლოების რაოდენობა. შემდეგ დაპრინტეთ არის თუ არა ერთმანეთის ტოლი სიმბოლოების რაოდენობა.
a = input("enter your str")
b = input("enyter your str")

c = 0
for i in a:
    c +=1

d = 0
for i in b:
    d +=1

print(c)
print(d)

if c == d:
    print("tolia")
else:
    print("ar aris toli")