my_list = [1, 2, 3, 4, 5]
try:
    num = my_list[5]
    print(num)
except Exception as err:
    print("Something went wrong: " + str(err))

#add type error



try:
    with open("some_file.txt", "r") as f:
        text = f.read()
        print(text)
    num = my_list[5]
except FileNotFoundError as err:
    print("Something went wrong: + " + str(err))
except IndexError as err2:
    print("Something")