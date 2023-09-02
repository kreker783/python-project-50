result = "{ \n"


def get_result(first_dict, second_dict):
    get_line(first_dict, second_dict)

    global result
    result += "}"
    return result


def get_line(first_dict, second_dict, indent=0):
    add_first_dict(first_dict, second_dict, indent)
    add_second_dict(first_dict, second_dict, indent)


def add_first_dict(arr1, arr2, indent):

    for _, (key, item) in enumerate(arr1.items()):
        if key in arr2 and item == arr2[key]:
            if if_dict(item, arr2[key]):
                add_nested_dict(key, item, arr2[key], indent)
            else:
                add_to_result(key, item, indent)
        elif key in arr2:
            if if_dict(item, arr2[key]):
                add_nested_dict(key, item, arr2[key], indent)
            elif if_dict(item):
                add_nested_dict(key, item, {}, indent)
            elif if_dict(arr2[key]):
                add_nested_dict(key, {}, arr2[key], indent)
            else:
                add_to_result(key, item, indent, sign="-")
                add_to_result(key, arr2[key], indent, sign="+")
        elif key not in arr2:
            not_in_arr(key, item, indent, "-")


def add_second_dict(first_dict, second_dict, indent=0):
    for _, (key, item) in enumerate(second_dict.items()):
        if key not in first_dict:
            not_in_arr(key, item, indent, "+")


def if_dict(*args):
    for item in args:
        if not isinstance(item, dict):
            return False
    return True


def add_nested_dict(key, item, item2, indent):
    add_to_result(key, "{", indent)

    indent += 4
    get_line(item, item2, indent)
    indent -= 4

    add_to_result("", "}", indent)


def not_in_arr(key, item, indent, sign):
    if if_dict(item):
        add_to_result(key, "{", indent, sign)
        for_not_in_arr(item, indent)
        add_to_result("", "}", indent)
    else:
        add_to_result(key, item, indent, sign)


def for_not_in_arr(item, indent):
    for _, (key, value) in enumerate(item.items()):
        if if_dict(value):
            indent += 4

            add_to_result(key, "{", indent)
            for_not_in_arr(value, indent)
            add_to_result("", "}", indent)

            indent -= 4
        else:
            add_to_result(key, value, indent + 5, sign="")


def add_to_result(key, value, indent, sign=" "):
    global result
    space = (indent + 2) * " "
    if value == "}":
        result += f'{space} {key} {value}\n'
    else:
        value = str(value).lower()
        result += f'{space}{sign} {key}: {value}\n'
