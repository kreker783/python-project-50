res = {}
temp_dict = {}


def get_line(first_dict, second_dict, temp=False):
    get_first_dict(first_dict, second_dict, temp=temp)

    for _, (key, item) in enumerate(second_dict.items()):
        if key not in first_dict:
            add_to_result(key, item, '+', temp=temp)

    global res
    return res


def get_first_dict(arr1, arr2, temp):

    for _, (key, item) in enumerate(arr1.items()):
        if key in arr2 and item == arr2[key]:
            add_to_result(key, item, temp)
        elif key in arr2:
            if isinstance(item, dict) and isinstance(arr2[key], dict):
                global temp_dict
                get_line(item, arr2[key], temp=True)
                add_to_result(key, temp_dict)
                temp_dict = {}
            else:
                add_to_result(key, item, "-", temp=temp)
                add_to_result(key, arr2[key], "+", temp=temp)
        elif key not in arr2:
            add_to_result(key, item, "-", temp=temp)


def add_to_result(key, value, sign=" ", temp=False):
    global res
    if not temp:
        res[f"{sign} {key}"] = value
    else:
        add_to_temp(key, value, sign)


def add_to_temp(key, value, sign):
    global temp_dict
    temp_dict[f"{sign} {key}"] = value
