import sys
from typing import Optional

from app.enums import CommandsEnum
from app.exceptions import MissingDependencyError
from app.todo_list import TodoList
from storage.interface import AbstractStorage


class TodoListController:
    def __init__(self, todo_items: TodoList, storage: Optional[AbstractStorage] = None):
        self.todo_items = todo_items
        self.storage = storage

    def loop(self):
        while True:
            print(
                "Please input the command for the todo list.\n"
                "To add type add, \n"
                "to show the current todo list type show,\n"
                "to complete an item type complete,\n"
                "to edit an item type edit \n"
                "and to exit type exit."
            )

            action = str.lower(input("Command: ")).strip()
            match action:
                case CommandsEnum.ADD.value:
                    while True:
                        todo_item = input(
                            "Enter the text for your new todo item, or enter 'back' to go back to command selection: "
                        )
                        if todo_item == "back":
                            break
                        self.todo_items.add(todo_item)
                        self.todo_items.show()

                case CommandsEnum.SHOW.value:
                    self.todo_items.show()
                case CommandsEnum.COMPLETE.value:
                    try:
                        item_index = input("Enter the index of the item you wish to complete: ")
                        item_index_adjusted = int(item_index) - 1
                        if item_index_adjusted <= 0:
                            item_index = input("Invalid index entered, please enter an index greater than 1.")
                        self.todo_items.complete(index=item_index_adjusted)
                    except ValueError:
                        print("Invalid index entered, please enter an index greater than 1.")
                case CommandsEnum.EDIT.value:
                    try:
                        while True:
                            item_index = input("Enter the index of the item you wish to edit from the list: ")
                            item_index_adjusted = int(item_index) - 1
                            if item_index_adjusted <= 0:
                                print("Invalid index entered, please enter an index greater than 1.")
                            else:
                                break
                        item_text = input("Enter the text to edit the item: ")
                        self.todo_items.edit(index=item_index_adjusted, text=item_text)
                    except ValueError:
                        print("Invalid index entered, please enter an index greater than 1.")
                case CommandsEnum.EXIT.value:
                    sys.exit(0)
                case _:
                    print("Action not recognized.")

    def store_todo_list(self):
        if not self.storage:
            raise MissingDependencyError()
        self.storage.save(self.todo_items.tasks)
