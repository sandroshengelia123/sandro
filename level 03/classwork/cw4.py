text1 = input("შეიყვანეთ პირველი სტრინგი: ")
text2 = input("შეიყვანეთ მეორე სტრინგი: ")

# სიმბოლოების დათვლა for loop-ით
count1 = 0
for _ in text1:
    count1 += 1

count2 = 0
for _ in text2:
    count2 += 1

print("პირველი სტრინგის სიგრძეა:", count1)
print("მეორე სტრინგის სიგრძეა:", count2)

# შედარება
if count1 == count2:
    print("ორივე სტრინგში სიმბოლოების რაოდენობა თანაბარია.")
else:
    print("სტრინგებში სიმბოლოების რაოდენობა განსხვავებულია.")
