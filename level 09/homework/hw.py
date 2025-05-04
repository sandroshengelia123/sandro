# 1
car = "mercedes"
car = car.capitalize()
print(car)

car2 = "toyota"
car3 = "honda"
print(car2.capitalize())
print(car3.capitalize())

# 2
fruit = "banani"
fruit = fruit.upper()
print(fruit)

fruit2 = "vashli"
fruit3 = "kivi"
print(fruit2.upper())
print(fruit3.upper())


# 3
country = "GEORGIA"
country = country.lower()
print(country)


# 4
city = "tbilisi"
index = city.find("s")
print(index)

city2 = "batumi"
print(city2.find("m"))

city3 = "kutaisi"
print(city3.find("i"))


# 5
items = ["ირაკლი", "ბექა", 50, "ატამი", 40.50, "თვითმფრინავი"]
print(items.index("ატამი"))
print(items.index(50))

items2 = ["ნატო", "კატა", 30, "ბანანი", "კრავი"]
print(items2.index("კატა"))
print(items2.index(30))

items3 = [10, "ლეპტოპი", "ჩანთა", 99.9]
print(items3.index("ჩანთა"))
print(items3.index(10))


# 6
names = ["giorgi", "nino", "ana"]
capitalized_names = [name.capitalize() for name in names]
print(capitalized_names)


# 7
countries = ["germany", "france", "italy"]
upper_countries = [country.upper() for country in countries]
print(upper_countries)


# 8
countries_upper = ["USA", "CANADA", "BRAZIL"]
lower_countries = [country.lower() for country in countries_upper]
print(lower_countries)
