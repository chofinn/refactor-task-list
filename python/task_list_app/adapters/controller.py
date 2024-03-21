from task_list_app.entities.task_list import TaskList
from task_list_app.use_cases.commands import *


class Controller:
    def __init__(self) -> None:
        self.task_list = TaskList()
        

    def execute(self, command_line: str) -> None:
        context = CommandContext()

        command, *args = command_line.split(" ", 1)
        if command == "show":
            context.set_command(ShowCommand(self.task_list))
        elif command == "add":
            context.set_command(AddCommand(self.task_list))
        elif command == "check":
            context.set_command(CheckCommand(self.task_list))
        elif command == "uncheck":
            context.set_command(UncheckCommand(self.task_list))
        elif command == "help":
            context.set_command(HelpCommand())
        else:
            context.set_command(ErrorCommand())
        return context.execute_command(args)