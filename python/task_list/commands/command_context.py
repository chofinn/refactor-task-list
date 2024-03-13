class CommandContext:
    def __init__(self):
        self._command = None
        self._console = None

    def set_command(self, command):
        self._command = command

    def execute_command(self, command: str=None):
        if self._command:
            self._command.execute(command)
        else:
            print("No command selected")
