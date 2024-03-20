from .command_interface import CommandInterface

class CheckCommand(CommandInterface):
    def __init__(self, task_list) -> None:
        self.task_list = task_list

    def execute(self, command: str=None) -> None:
        self.task_list.set_state(int(command), True)