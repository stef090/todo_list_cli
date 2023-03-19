from enum import Enum
from typing import List


class CommandsEnum(Enum):
    ADD = "add"
    SHOW = "show"
    DELETE = "delete"
    EDIT = "edit"
    EXIT = "exit"

    @classmethod
    def values(cls) -> List[str]:
        commands = [command.value for command in CommandsEnum]
        return commands
