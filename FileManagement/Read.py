print("The whole file:-----------")
with open("Example.txt") as f:
    text = f.read()
    print(text + "\n")

print("One line:-----------")
with open("Example.txt") as f:
    line = f.readline()
    line2 = f.readline()
    print(line)

print("Each line:-----------")
with open("Example.txt") as f:
    lines = f.readlines()
    print(lines)

print("Loop over file:-----------")
with open("Example.txt") as f:
    for x in f:
        print(x)




