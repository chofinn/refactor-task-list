from .command_interface import CommandInterface

class ErrorCommand(CommandInterface):
    def __init__(self, console) -> None:
        self.console = console

    def execute(self, command: str=None) -> None:
        self.console.print(f"I don't know what the command {command} is.")
        self.console.print()