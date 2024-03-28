from .command_interface import CommandInterface

class ErrorCommand(CommandInterface):
    def __init__(self, unknownCmd: str) -> None:
        self.unknownCmd = unknownCmd

    def execute(self, command: str=None) -> None:
        return f"I don't know what the command {self.unknownCmd} is.\n"