def find_item(item_list, my_item):
    found_item_list = []
    for item in item_list:
        if item == my_item:
            pos = item.pos()
            found_item_list.append(pos)
    return found_item_list
