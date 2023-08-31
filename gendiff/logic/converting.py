res = "{ \n"


def get_line(first_dict, second_dict, indent=0):
    get_first_dict(first_dict, second_dict, indent)

    for _, (key, item) in enumerate(second_dict.items()):
        if key not in first_dict:
            if if_dict(item):
                add_nested_dict(key, item, {}, indent)
            else:
                add_to_result(key, item, indent, sign='+')

    global res
    # res += "}"
    return res


def get_first_dict(arr1, arr2, indent):

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
            if if_dict(item):
                add_nested_dict(key, item, {}, indent)
            else:
                add_to_result(key, item, indent, sign="-")


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


def add_to_result(key, value, indent, sign=" "):
    global res
    space = (indent + 2) * " "
    if value == "}":
        res += f'{space} {key} {value}\n'
    else:
        res += f'{space}{sign} {key}: {value}\n'

