def get_line(first_dict, second_dict):
    result = get_first_dict(first_dict, second_dict)

    for _, (key, item) in enumerate(second_dict.items()):
        if key not in first_dict:
            result += f"  + {key}: {item}\n"

    result += "}"

    return result


def get_first_dict(arr1, arr2):
    result = '{\n'

    for _, (key, item) in enumerate(arr1.items()):
        if key in arr2 and item == arr2[key]:
            result += f"    {key}: {item}\n"
        elif key in arr2:
            result += f"  - {key}: {item}\n"
            result += f"  + {key}: {arr2[key]}\n"
        elif key not in arr2:
            result += f"  - {key}: {item}\n"

    return result
