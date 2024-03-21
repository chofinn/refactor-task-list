from .command_interface import CommandInterface

class ErrorCommand(CommandInterface):
    def execute(self, command: str=None) -> None:
        return f"I don't know what the command {command} is."