from task_list_app.use_cases.commands import *
from task_list_app.adapters.presenter import Presenter


class Controller:
    def __init__(self, task_list) -> None:
        self.task_list = task_list
        
    def execute(self, console, command_line: str) -> None:
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
            context.set_command(ErrorCommand(command))
        
        presenter = Presenter(console)
        presenter.present(context.execute_command(args))