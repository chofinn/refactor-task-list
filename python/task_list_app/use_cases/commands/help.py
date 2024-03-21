from .command_interface import CommandInterface

class HelpCommand(CommandInterface):
    def __init__(self, console) -> None:
        self.console = console

    def execute(self, command: str=None) -> None:
        result = ""
        result += "Commands:\n"
        result += "  show\n"
        result += "  add project <project name>\n"
        result += "  add task <project name> <task description>\n"
        result += "  check <task ID>\n"
        result += "  uncheck <task ID>\n"
        return result