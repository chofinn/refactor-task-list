class CommandContext:
    def __init__(self):
        self._command = None
        self._console = None

    def set_command(self, command):
        self._command = command

    def execute_command(self, command: str=None):
        if self._command:
            return self._command.execute(command[0] if command else "")
        else:
            return "No command selected\n"
