from gendiff.scripts.gendiff import generate_diff


def test_gendiff_yaml():
    first_path = "gendiff/files/yaml/file1.yaml"
    second_path = "gendiff/files/yaml/file2.yml"
    result = """{
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
}"""
    assert generate_diff(first_path, second_path) == result


def test_gendiff_json():
    first_path = "gendiff/files/json/file1.json"
    second_path = "gendiff/files/json/file2.json"
    result = """{
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
}"""
    assert generate_diff(first_path, second_path) == result

