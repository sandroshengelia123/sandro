# ომხმარებელს შემოატანინე მისი საყვარელი ფერი,თუ საყვარელი ფერი ემთხვევა წითელს ტერმინალში გამოუტანე red is favorite color,თუ შემოტანილი ფერი ემთხვევა ყვითელს დაუპტინტე favorite color is yellow,თუ შემოტანილი ფერი ემთხვევა ლურჯს დაუპრინტე favorite color is blue,ყველა სხვა დანარჩენ შემთხვევაში დაუპტინტე other color
color = input("enter color")
if color == "red":
    print("red is favorite color")
elif color == "yellow":
    print("favorite color is yellow")
elif color == "blue":
    print("favorite color is blue")
else:
    print("other color")