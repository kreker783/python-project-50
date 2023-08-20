import argparse
import json


parser = argparse.ArgumentParser(
    prog="gendiff",
    description="Compares two configuration files and shows a difference."
)

parser.add_argument(
    "first_file",
    type=str
)
parser.add_argument(
    "second_file",
    type=str
)
parser.add_argument(
    "-f",
    "--format",
    action="append",
    help="set format of output")

args = parser.parse_args()


def main():
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


def generate_diff(first_path, second_path):
    first_file = json.load(open(first_path))
    second_file = json.load(open(second_path))

    first_file = sort_dict(first_file)
    second_file = sort_dict(second_file)

    return get_line(first_file, second_file)


def sort_dict(arr):
    return dict(sorted(arr.items()))


def get_line(first_dict, second_dict):
    result = get_first_dict(first_dict, second_dict)

    # for _, (key, item) in enumerate(first_dict.items()):
    #     if key in second_dict and item == second_dict[key]:
    #         result += f"    {key}: {item}\n"
    #     elif key in second_dict:
    #         result += f"  - {key}: {item}\n"
    #         result += f"  + {key}: {second_dict[key]}\n"
    #     elif key not in second_dict:
    #         result += f"  - {key}: {item}\n"

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


if __name__ == "__main__":
    main()
