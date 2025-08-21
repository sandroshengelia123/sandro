# შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი სიტყვა. ხმოვნები სადაც იქნება ! ნიშნით ჩაინაცვლოს და თანხმოვნები *-ით სხვა დანარჩენი სიმბოლო იყოს ისე როგორ იქნება. 
def gamarjoba(userword):
  result = ""  
  for i in userword:
    if i in "aeiou":
      result +="!"
    elif i in "mgjbrdtwvxyzchnflkpq":
      result +="*"
    else:
      result += i
  print(result)
gamarjoba("hello")