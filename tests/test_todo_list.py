from app.todo_list import TodoList


class TestTodoList:
    def setup(self):
        self.todo_list = TodoList()

    def test_add_new_item_to_todo_list(self):
        self.todo_list.add("Test TODO")
        assert len(self.todo_list.tasks) == 1
        assert self.todo_list.tasks[0] == "Test TODO"

        self.todo_list.add("Test TODO 2")
        assert len(self.todo_list.tasks) == 2
        assert self.todo_list.tasks[1] == "Test TODO 2"

    def test_show_todo_list(self):
        self.todo_list.add("Test TODO")

        todo_list_printed = self.todo_list.show()
        assert "Test TODO" in todo_list_printed

    def test_delete_item_from_todo_list(self):
        self.todo_list.add("New Task")
        self.todo_list.add("New Task 2")

        self.todo_list.delete(0)
        assert len(self.todo_list) == 1
