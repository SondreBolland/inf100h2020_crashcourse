# Lag en funksjon for det største elementet i en liste
def max(my_list):
    max_element = -999999
    for element in my_list:
        if element > max_element:
            max_element = element
    print(max_element)
    return max_element

my_list = [5, 7, -400, 1000, 544]
max_element = max(my_list)









def max(my_list):
    largest_element = -99999
    for element in my_list:
        if element > largest_element:
            largest_element = element
    return largest_element

list_of_integers = [-440, 100, 4, 123, 96, 0]
largest_integer = max(list_of_integers)
print("The largest integer of my list was: " + str(largest_integer))

# Legg til et element i en liste
def append(old_list, new_element):
    size_of_new_list = len(old_list) + 1
    new_list = [None] * size_of_new_list
    for index, elem in enumerate(old_list):
        new_list[index] = elem
    new_list[-1] = new_element
    return new_list

my_list = ["kake", "kaffe", "telefon"]
next_word = "laptop"
my_new_list = append(my_list, next_word)
print(my_new_list)