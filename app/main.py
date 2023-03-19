import sys
from enums import CommandsEnum
from todo_list import TodoList

if __name__ == "__main__":
    todo_list = TodoList()
    while True:
        print(
            "Please input the command for the todo list.\n"
            "To add type add, \n"
            "to show the current todo list type show,\n"
            "to delete an item type delete,\n"
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
                    todo_list.add(todo_item)
                    todo_list.show()

            case CommandsEnum.SHOW.value:
                todo_list.show()
            case CommandsEnum.DELETE.value:
                try:
                    item_index = input("Enter the index of the item you wish to delete from the list: ")
                    item_index_adjusted = int(item_index) - 1
                    if item_index_adjusted <= 0:
                        item_index = input("Invalid index entered, please enter an index greater than 1.")
                    todo_list.delete(index=item_index_adjusted)
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
                    todo_list.edit(index=item_index_adjusted, text=item_text)
                except ValueError:
                    print("Invalid index entered, please enter an index greater than 1.")
            case CommandsEnum.EXIT.value:
                sys.exit(0)
            case _:
                print("Action not recognized.")
