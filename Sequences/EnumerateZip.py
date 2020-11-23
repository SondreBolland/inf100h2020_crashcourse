my_list = ["kake", "mus", "eple", "høytaler"]
enumerate_list = enumerate(my_list)
print(str(list(enumerate_list)) + "\n")

for index in range(len(my_list)):
    current_element = my_list[index]
    print("Current element:" + str(current_element))

for element in my_list:
    current_index = my_list.index(element)
    print("Current index:" + str(current_index))

for index, element in enumerate(my_list):
    print("Current index is: " + str(index))
    print("Current element is: " + str(element))
