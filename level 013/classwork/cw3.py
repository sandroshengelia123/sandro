# შექმენით ფუნქცია რომელსაც არგუმენტად სია, ამ სიაში უნდა იყოს სხვადასხვა ტიპის მონაცემები და დაითვალოს რამდენი სტრინგ ტიპის მონაცემი არი
def count_letters(word):
    count = 0
    for i in word:
        count += 1
    return count
print(count_letters("word"))