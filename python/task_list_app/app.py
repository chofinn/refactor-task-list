from task_list_app.io.console import Console
from task_list_app.adapters.controller import Controller


class TaskListApp:
    QUIT = "quit"

    def __init__(self, console: Console) -> None:
        self.console = console
        self.controller: Controller = Controller()

    def run(self) -> None:
        while True:
            command = self.console.input("> ")
            if command == self.QUIT:
                break
            output = self.controller.execute(command)
            if output:
                self.console.print(output)