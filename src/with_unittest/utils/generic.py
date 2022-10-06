import copy

def copy_list(input_list):
    list = []
    for i in range(len(input_list)):
        list.append(copy.copy(input_list[i]))
    return list
