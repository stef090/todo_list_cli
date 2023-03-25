import os

from storage.file_storage import FileStorage


class TestFileStorage:
    def test_file_storage(self):
        if not os.path.exists("test_files"):
            os.mkdir("test_files")
        file_path = "test_files/test_file.txt"
        file_storage = FileStorage(file_path=file_path)
        item_list = ["Item 1", "Item 2", "Item 3"]
        file_storage.save(item_list)
        for item in item_list:
            with open("test_file.txt", "r") as f:
                actual_contents = f.read()
                assert item in actual_contents

    def test_file_storage_invalid_file_path(self):
        pass
