filename = "foo.txt"
with open(filename) as f:
    for line in f:
        line = line.strip()
        line = line[::-1]
        print(line)