from task_list_app.entities.task_list import TaskList
from task_list_app.io.console import Console
from task_list_app.adapters.controller import Controller


class TaskListApp:
    QUIT = "quit"

    def __init__(self, console: Console) -> None:
        self.console = console
        self.task_list = TaskList()
        self.controller: Controller = Controller(self.task_list)

    def run(self) -> None:
        while True:
            command = self.console.input("> ")
            if command == self.QUIT:
                break
            self.controller.execute(self.console, command)