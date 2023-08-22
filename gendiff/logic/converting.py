result = {}


def get_line(first_dict, second_dict):
    get_first_dict(first_dict, second_dict)

    for _, (key, item) in enumerate(second_dict.items()):
        if key not in first_dict:
            add_to_result(key, item, '+')

    global result
    return result


def get_first_dict(arr1, arr2):

    for _, (key, item) in enumerate(arr1.items()):
        if key in arr2 and item == arr2[key]:
            add_to_result(key, item)
        elif key in arr2:
            add_to_result(key, item, "-")
            add_to_result(key, arr2[key], "+")
        elif key not in arr2:
            add_to_result(key, item, "-")


def add_to_result(key, value, sign=" "):
    global result
    result[f"{sign} {key}"] = value
