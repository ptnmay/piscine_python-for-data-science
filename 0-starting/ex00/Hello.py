ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list[1] = "World!"

#rebuild
# ft_tuple = (ft_tuple[0],"42Hongkong")

tmp_list = list(ft_tuple)
tmp_list[1] = "Thailand!"
ft_tuple = tuple(tmp_list)

#print order is unpredictable
ft_set.remove("tutu!")
ft_set.add("Bangkok!")

ft_dict["Hello"] = "42Bangkok!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)