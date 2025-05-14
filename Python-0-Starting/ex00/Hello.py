ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Working with list
ft_list[1] = "World!"

# Tuples are a type of data structure in Python that, once created, cannot be modified.
ft_tuple = ("Hello", "Deutschland!")

# Sets are unordered collections of unique elements.
# For sets, first remove the old element and add the new one
ft_set.remove("tutu!")
ft_set.add("Heilbronn!")

# For dictionary, update the value
ft_dict["Hello"] = "42Heilbronn!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)