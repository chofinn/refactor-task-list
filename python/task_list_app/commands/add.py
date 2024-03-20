from typing import Dict
from .command_interface import CommandInterface
from task_list_app.entities.task import Task
from task_list_app.console import Console
from task_list_app.entities.project import Project

class AddCommand(CommandInterface):
    def __init__(self, console: Console, task_list) -> None:
        self.console = console
        self.task_list = task_list
        
        
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
        self.task_list.add_project(name)

    def add_task(self, project: str, description: str) -> None:
        self.task_list.add_task(project, description)

    def error_msg(self):
        self.console.print("wrong argument, usage: add project <prj_name>, add task <prj_name> <task_name>")