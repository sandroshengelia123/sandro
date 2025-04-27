# 1
string_list = ["apple", "banana", "cherry", "grape"]

# 2
integer_list = [10, 20, 30, 40, 50]

# 3
float_list = [1.1, 2.5, 3.14, 4.0, 5.75]

# 4
mixed_list = ["hello", 100, 3.14, False]

# 5
my_list = ["cat", "purple", 21, 150.6, True]

# ინდექსები:
# "cat"     -> ინდექსი 0
# "purple"  -> ინდექსი 1
# 21        -> ინდექსი 2
# 150.6     -> ინდექსი 3
# True      -> ინდექსი 4



# 1
my_list = ["fortoxali", "gvanca", 150.6, True]

print(my_list[0])  # fortoxali
print(my_list[1])  # gvanca
print(my_list[2])  # 150.6
print(my_list[3])  # True

# 2
my_list = ["fortoxali", "gvanca", 150.6, True]

my_list[0] = "apple"  # ჩანაცვლება

print(my_list)  # ['apple', 'gvanca', 150.6, True]

# 3
my_list = ["fortoxali", "gvanca", 150.6, "tkbili", True]

result = my_list[3] + my_list[0]  # "tkbili" + "fortoxali"
print(result)  # tkbilifortoxali
