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

    def delete(self, index: int) -> None:
        try:
            del self.tasks[index]
        except IndexError:
            print(f"No item present at index {index + 1}")

    def add(self, text: str) -> None:
        self.tasks.append(text)

    def edit(self, index: int, text: str) -> None:
        pass

    def show(self) -> str:
        print(self)
        return self.__str__()
