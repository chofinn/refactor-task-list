from typing import Dict, List
from task_list.task import Task
from task_list.project import Project
from task_list.task_list import TaskList
from task_list.console import Console
from .commands import *


class Command:
    def __init__(self, console: Console) -> None:
        self.console = console
        self.task_list = TaskList()
        

    def execute(self, command_line: str) -> None:
        context = CommandContext()

        command, *args = command_line.split(" ", 1)
        if command == "show":
            context.set_command(ShowCommand(self.console, self.task_list))
        elif command == "add":
            context.set_command(AddCommand(self.console, self.task_list))
        elif command == "check":
            context.set_command(CheckCommand(self.task_list))
        elif command == "uncheck":
            context.set_command(UncheckCommand(self.task_list))
        elif command == "help":
            context.set_command(HelpCommand(self.console))
        else:
            context.set_command(ErrorCommand(self.console))
        context.execute_command(args)