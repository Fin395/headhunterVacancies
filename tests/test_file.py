from src.file import FileManager


def test_file_init():
    file = FileManager("my_json_file")
    assert file.name == "my_json_file"