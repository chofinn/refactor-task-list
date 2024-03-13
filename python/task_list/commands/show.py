from typing import Dict
from .command_interface import CommandInterface
from task_list.console import Console

class ShowCommand(CommandInterface):
    def __init__(self, console: Console, tasks: Dict) -> None:
        self.console = console
        self.tasks = tasks

    def execute(self, command: str=None) -> None:
        for project, tasks in self.tasks.items():
            self.console.print(project)
            for task in tasks:
                self.console.print(f"  [{'x' if task.is_done() else ' '}] {task.id}: {task.description}")
            self.console.print()