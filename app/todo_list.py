class TodoList:
    def __init__(self) -> None:
        self.tasks = []

    def __str__(self) -> str:
        output_list = ["\nYour TODO list: \n"]
        for index, item in enumerate(self.tasks):
            output_list.append(f"\t{index + 1}. {item}\n")
        return "".join(output_list)

    def __len__(self) -> int:
        return len(self.tasks)

    def complete(self, index: int) -> None:
        try:
            self.tasks.pop(index)
        except IndexError as exc:
            print(f"No item present at index {index + 1}")
            raise exc

    def add(self, text: str) -> None:
        self.tasks.append(text)

    def edit(self, index: int, text: str) -> None:
        try:
            self.tasks[index] = text
        except IndexError as exc:
            print(f"No item present at index {index + 1}")
            raise exc

    def show(self) -> str:
        print(self)
        return self.__str__()
