from typing import Dict, List

from task_list.console import Console
from task_list.task import Task
from task_list.command import Command


class TaskList:
    QUIT = "quit"

    def __init__(self, console: Console) -> None:
        self.console = console
        self.last_id: int = 0
        self.tasks: Dict[str, List[Task]] = dict()
        self.cmd: Command = Command(console)

    def run(self) -> None:
        while True:
            command = self.console.input("> ")
            if command == self.QUIT:
                break
            self.cmd.execute(command)

    def set_done(self, id_string: str, done: bool) -> None:
        id_ = int(id_string)
        for project, tasks in self.tasks.items():
            for task in tasks:
                if task.id == id_:
                    task.set_done(done)
                    return
        self.console.print(f"Could not find a task with an ID of {id_}")
        self.console.print()