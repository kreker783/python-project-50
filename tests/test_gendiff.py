from gendiff.scripts.gendiff import generate_diff


def test_gendiff():
    first_path = "gendiff/files/file1.json"
    second_path = "gendiff/files/file2.json"
    result = """
{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
    assert generate_diff(first_path, second_path) == result

