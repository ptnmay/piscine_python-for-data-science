ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# list
ft_list[1] = "World!"

# tuple
tmp_list = list(ft_tuple)
tmp_list[1] = "Thailand!"
ft_tuple = tuple(tmp_list)

# set
ft_set.remove("tutu!")
ft_set.add("Bangkok!")

# dict
ft_dict["Hello"] = "42Bangkok!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
