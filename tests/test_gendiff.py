from gendiff.scripts.gendiff import generate_diff


def test_gendiff():
    first_path = "/home/kreker/Projects/python-project-50/gendiff/files/file1.json"
    second_path = "/home/kreker/Projects/python-project-50/gendiff/files/file2.json"
    result = """{
                    - follow: false
                    host: hexlet.io
                    - proxy: 123.234.53.22
                    - timeout: 50
                    + timeout: 20
                    + verbose: true
                }"""
    assert generate_diff(first_path, second_path) == result

