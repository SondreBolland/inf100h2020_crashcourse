def all_same(input):
    x = input[0]
    for e in input[1:]:
        if x != e:
            return False
    return True

