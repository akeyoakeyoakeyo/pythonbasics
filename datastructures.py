# list data structures
my_list = ["Kenya", "Niger","Tanzania","Vietnam", "Djibouti", "Mozambique", "Seychelles"]
print(my_list)
print(my_list[3])
print(f"I am from {my_list[0]}")

my_list[1] = "Mali"
print(my_list)
my_list.sort()
print(my_list)
my_num = [2,56,93,27,98,100]
print(my_num)
my_num.sort()
print(my_num)

# tuple data structures
my_tuple = ("apples", "grapes", "mangoes", "oranges", "watermelon", "pears" )
print(my_tuple)
my_tuple[1] == "berries"
print(my_tuple)

# set data structure
my_set = {"Lamborghini", "Benz", "Tesla", "Honda", "Subaru" }
print(my_set)

# dictionaries data structure
my_dic = {"name":"Erick", "age":"47", "gender":"male"}
print(my_dic)
print(f"My age is {my_dic['age']}")
my_dic.pop('gender')
print(my_dic)