from typing import Dict, List
from task_list.task import Task
from task_list.console import Console
from .commands import *

class Command:
    def __init__(self, console: Console) -> None:
        self.console = console
        self.tasks: Dict[str, List[Task]] = dict()
        self.console.print("start")

    def execute(self, command_line: str) -> None:
        context = CommandContext()

        command, *args = command_line.split(" ", 1)
        if command == "show":
            context.set_command(ShowCommand(self.console, self.tasks))
        elif command == "add":
            context.set_command(AddCommand(self.console, self.tasks))
        elif command == "check":
            context.set_command(CheckCommand(self.tasks))
        elif command == "uncheck":
            context.set_command(UncheckCommand(self.tasks))
        elif command == "help":
            context.set_command(HelpCommand(self.console))
        else:
            context.set_command(ErrorCommand(self.console))
        context.execute_command(args)
