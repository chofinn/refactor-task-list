from typing import Dict
from .command_interface import CommandInterface
from task_list.console import Console

class ShowCommand(CommandInterface):
    def __init__(self, console: Console, task_list) -> None:
        self.console = console
        self.task_list = task_list

    def execute(self, command: str=None) -> None:
        for project in self.task_list.get_all_projects():
            self.console.print(project.get_name())
            for task in project.get_all_tasks():
                self.console.print(f"  [{'x' if task.is_done() else ' '}] {task.id}: {task.description}")
            self.console.print()