my_dict={
    "name":"gousiya",
    "age":21,
    "occupation":"student"
}
print(type(my_dict))
print(my_dict["name"])
my_dict["name"]="shaik gousia"
print(my_dict["name"])
update_name={
    "name":"gousiyashaik"
}
my_dict.update(update_name)
print(my_dict["name"])