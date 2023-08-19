import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument(
        "first_file",
        type=argparse.FileType('r')
    )
    parser.add_argument(
        "second_file",
        type=argparse.FileType('r')
    )
    parser.add_argument(
        "-f",
        "--format",
        action="append",
        help="set format of output")

    args = parser.parse_args()

    for f in vars(args):
        print(f)


if __name__ == "__main__":
    main()
