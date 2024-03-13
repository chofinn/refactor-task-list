from task_list.console import Console
from .commands import *

class Command:
    def __init__(self, console: Console) -> None:
        self.console = console
        self.last_id: int = 0
        self.console.print("start")

    def execute(self, command_line: str) -> None:
        context = CommandContext()

        command_list = command_line.split(" ", 1)
        command = command_list[0]
        if command == "show":
            context.set_command(ShowCommand(self.console))
        elif command == "add":
            context.set_command(AddCommand(self.console))
        elif command == "check":
            context.set_command(CheckCommand())
        elif command == "uncheck":
            context.set_command(UncheckCommand())
        elif command == "help":
            context.set_command(HelpCommand(self.console))
        else:
            context.set_command(ErrorCommand(self.console))
        context.execute_command(command_line)
