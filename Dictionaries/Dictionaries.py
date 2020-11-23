my_dict = {}
my_other_dict = dict()

my_dict = {0: 5, 1: 17, 2: 4, 3: -40, 4: 10}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dict = {"one": [1,2,3], 10: 17, "kake": 4, "inf100": -40, "læll": 10}
print(my_dict.keys())
print(my_dict.values())

print(my_dict["one"])
my_dict["one"] = 100
print(my_dict["one"])
my_dict.update({"youtube": 400})
print(my_dict)