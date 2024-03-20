from .command_interface import CommandInterface

class HelpCommand(CommandInterface):
    def __init__(self, console) -> None:
        self.console = console

    def execute(self, command: str=None) -> None:
        self.console.print("Commands:")
        self.console.print("  show")
        self.console.print("  add project <project name>")
        self.console.print("  add task <project name> <task description>")
        self.console.print("  check <task ID>")
        self.console.print("  uncheck <task ID>")
        self.console.print()