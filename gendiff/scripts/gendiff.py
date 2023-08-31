import argparse
import json

from gendiff.logic.converting import get_line
import gendiff.logic.file_format as ff


parser = argparse.ArgumentParser(
    prog="gendiff",
    description="Compares two configuration files and shows a difference."
)

parser.add_argument(
    "first_file",
    type=str,
    nargs='?'
)
parser.add_argument(
    "second_file",
    type=str,
    nargs='?'
)
parser.add_argument(
    "-f",
    "--format",
    action="append",
    help="set format of output")

args = parser.parse_args()


def main():
    if args.first_file and args.second_file:
        diff = generate_diff(args.first_file, args.second_file)
        print(diff)


def generate_diff(first_path, second_path):
    first_file, second_file = ff.get_dict_from_file(first_path, second_path)
    result = get_line(first_file, second_file)
    return result


if __name__ == "__main__":
    main()
