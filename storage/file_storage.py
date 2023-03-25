from typing import List

from storage.interface import AbstractStorage


class FileStorage(AbstractStorage):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save(self, item_list: List[str]):
        with open(file=self.file_path, mode="w") as file:
            for item in item_list:
                file.writelines(f"{item}\n")

    def read(self) -> List[str]:
        with open(file=self.file_path, mode="w") as file:
            file.read()
