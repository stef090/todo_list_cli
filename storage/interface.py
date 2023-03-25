from abc import ABC
from typing import List


class AbstractStorage(ABC):
    def save(self, item_list: List[str]) -> None:
        ...

    def read(self) -> List[str]:
        ...
