from .command_interface import CommandInterface

class CheckCommand(CommandInterface):
    def execute(self, command: str=None) -> None:
        self.set_done(id_string, True)