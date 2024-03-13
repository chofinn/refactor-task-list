from .command_interface import CommandInterface
from task_list.console import Console

class ErrorCommand(CommandInterface):
    def __init__(self, console: Console) -> None:
        self.console = console

    def execute(self, command: str=None) -> None:
        self.console.print(f"I don't know what the command {command} is.")
        self.console.print()