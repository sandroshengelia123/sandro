# მომხმარებელს შემოატანინე სახელი. რასაც შემოიტანს მომხმარებელი ეგ გაამრავლე 5-ზე (ანუ დავუშვათ შემოიტანა d მაშინ ddddd რომ მიიღოთ) შეინახე ახალ ცვლადში და შემდეგ შეამოწმე ამ ახალი ცვლადის მნიშვნელობა სტრინგი არის თუ ინტეჯერი. (or ოპერატორი გამოიყენეთ)

name = input("enter your name ")
multiplayed_name = name * 5
print(type(multiplayed_name) == int or type(multiplayed_name == str))