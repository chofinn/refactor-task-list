from .command_interface import CommandInterface

class UncheckCommand(CommandInterface):
    def execute(self, command: str=None) -> None:
        self.set_done(id_string, False)