# 1
cars = ["Toyota", "BMW", "Mercedes", "Audi"]

# 2
numbers_int = [10, 20, 30, 40]

# 3
numbers_float = [1.5, 2.7, 3.14, 10.0]

# 4
mixed_list = ["hello", 100, 3.14, True]

# ინდექსები კომენტარებით:
# "hello"   -> ინდექსი  0  და -4
# 100       -> ინდექსი  1  და -3
# 3.14      -> ინდექსი  2  და -2
# True      -> ინდექსი  3  და -1

# 5
data = ["text", 25, 4.5, False]

print(data[0])  # text
print(data[1])  # 25
print(data[2])  # 4.5
print(data[3])  # False

# 6
all_data = ["sample", 100, 3.3, True]
print(all_data)  # ['sample', 100, 3.3, True]

# 7
info = ["გიორგი", 15 , 50.50 , "წლის"]
print(info[0], info[1], info[3])  # გიორგი 15 წლის

# 8
my_list = ["აკადემია", 50 , "ბექა" , 60.5 , "ირაკლი"]

# მენჯულე ინდექსზე (2) იყოს "გოა"
my_list[2] = "გოა"

# ბოლო ინდექსზე (4 ან -1) იყოს "საბა"
my_list[-1] = "საბა"

print(my_list)
# ['აკადემია', 50, 'გოა', 60.5, 'საბა']
