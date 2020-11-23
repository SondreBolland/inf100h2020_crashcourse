def min(input):
    a = input[0]
    for i in input[1:]:
        if i < a:
            a = i
    return a

