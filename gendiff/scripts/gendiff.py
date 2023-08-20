import argparse
from pathlib import Path
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


def generate_diff():
    first_file = json.load(open(args.first_file))
    second_file = json.load(open(args.second_file))

    first_file = sort_dict(first_file)
    second_file = sort_dict(second_file)

    result = '{\n'

    for _, (key, item) in enumerate(first_file.items()):
        if key in second_file and item == second_file[key]:
            result += f"    {key}: {item}\n"
        elif key in second_file:
            result += f"  - {key}: {item}\n"
            result += f"  + {key}: {second_file[key]}\n"
        elif key not in second_file:
            result += f"  - {key}: {item}\n"

    for _, (key, item) in enumerate(second_file.items()):
        if key not in first_file:
            result += f"  + {key}: {item}\n"

    result += "}"
    print(result)


def sort_dict(arr):
    return dict(sorted(arr.items()))


if __name__ == "__main__":
    generate_diff()
