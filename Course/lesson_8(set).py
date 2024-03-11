# set => '{}' No duplicate value

utensils = {"fork", "spoon", "knife"}
print(utensils)
# {'fork', 'spoon', 'knife'}
utensils.add("fork")
print(utensils)
# {'fork', 'spoon', 'knife'}

utensils.remove("fork")
utensils.clear()

frut = {"apple", "orange", 'watermenlon'}
dish = {"pizza", "hambergur"}
print(dish.union(frut))

print("the difference is {}".format(dish.difference(frut)))
