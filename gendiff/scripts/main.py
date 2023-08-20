from gendiff.scripts.gendiff import generate_diff


def main():
    first_path = "gendiff/files/file1.json"
    second_path = "gendiff/files/file2.json"
    diff = generate_diff(first_path, second_path)
    print(diff)


if __name__ == "__main__":
    main()
