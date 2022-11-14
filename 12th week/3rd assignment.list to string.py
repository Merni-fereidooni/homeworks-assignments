def string_to_list(string):
    list = []
    string.split(",")
    for i in string:
        list.append(i)

def list_to_string(list):
    string = None
    for i in list:
        string += list[i]