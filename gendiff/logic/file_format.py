import json
import yaml
from re import search


def get_dict_from_file(first_path, second_path):
    # get file format (json, yaml...)
    file_format = search("([^.]*$)", first_path).group(0)

    print(file_format)

    parsed_first_file = ""
    parsed_second_file = ""

    if file_format == "json":
        parsed_first_file = json.load(open(first_path))
        parsed_second_file = json.load(open(second_path))
    elif file_format == "yaml" or file_format == "yml":
        parsed_first_file = parse_yaml(first_path)
        parsed_second_file = parse_yaml(second_path)

    return sort_dict(parsed_first_file, parsed_second_file)


def sort_dict(arr1, arr2):
    arr1 = dict(sorted(arr1.items()))
    arr2 = dict(sorted(arr2.items()))
    return arr1, arr2


def parse_yaml(file):
    with open(file, 'r') as stream:
        try:
            parsed_file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return parsed_file
