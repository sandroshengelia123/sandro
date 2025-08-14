#  შექმენით ფუნქცია, რომესლაც გადაეცემა მომხმარებლის შემოტანილი ტექსტი და დაითვლით ასო 'a'-ს რაოდენობას. (დიდადაც რომ იყოს დაწერილი ისიც რომ ჩაითვალოს). 
def atis_raodenoba(text):
    return text.lower().count("a")

txt = input("enter text")
print("ასო 'a'-ს რაოდენობაა:", atis_raodenoba(txt))