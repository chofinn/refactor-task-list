from typing import Dict
from .command_interface import CommandInterface
from task_list.task import Task
from task_list.console import Console

class AddCommand(CommandInterface):
    def __init__(self, console: Console, tasks: Dict) -> None:
        self.console = console
        self.tasks = tasks
        self.last_id: int = 0
        
    def execute(self, command: str=None) -> None:
        sub_command_rest = command.split(" ", 1)
        if (len(sub_command_rest) != 2):
            self.error_msg()
        sub_command = sub_command_rest[0]
        if sub_command == "project":
            self.add_project(sub_command_rest[1])
        elif sub_command == "task":
            project_task = sub_command_rest[1].split(" ", 1)
            if (len(project_task) != 2):
                self.error_msg()
                return
            self.add_task(project_task[0], project_task[1])
        else:
            self.error_msg()
    
    def add_project(self, name: str) -> None:
        self.tasks[name] = []

    def add_task(self, project: str, description: str) -> None:
        project_tasks = self.tasks.get(project)
        if project_tasks is None:
            self.console.print(f"Could not find a project with the name {project}.")
            self.console.print()
            return
        project_tasks.append(Task(self.next_id(), description, False))

    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def error_msg(self):
        self.console.print("wrong argument, usage: add project <prj_name>, add task <prj_name> <task_name>")