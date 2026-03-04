ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# list -> changable, index, duplicate
ft_list[1] = "World!"

# tuple -> unchangable, index, duplicate
tmp_list = list(ft_tuple)
tmp_list[1] = "Thailand!"
ft_tuple = tuple(tmp_list)

# set -> unchangable, unindex, unique
ft_set.remove("tutu!")
ft_set.add("Bangkok!")

# dict -> changable, index, unique, like dictionary
ft_dict["Hello"] = "42Bangkok!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
