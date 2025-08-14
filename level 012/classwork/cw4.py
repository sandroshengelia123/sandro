# მომხმარებელს შემოატანინეთ ტექსტი და ამ ტექსტში დაითვალეთ რიცხვების რაოდენობა.
text = input("enter text")
count = 0
for i in text:
    if text.count("a"):
        count += 1
    print(count)