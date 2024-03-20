from task_list_app.io.console import Console
from task_list_app.adapters.command import Command


class TaskListApp:
    QUIT = "quit"

    def __init__(self, console: Console) -> None:
        self.console = console
        self.cmd: Command = Command(console)

    def run(self) -> None:
        while True:
            command = self.console.input("> ")
            if command == self.QUIT:
                break
            self.cmd.execute(command)