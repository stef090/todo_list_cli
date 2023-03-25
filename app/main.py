from app.controller import TodoListController
from todo_list import TodoList

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list_controller = TodoListController(todo_items=todo_list)
    todo_list_controller.loop()
