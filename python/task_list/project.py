from task_list.task import Task
from typing import List

class Project:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks = []
    
    def get_name(self) -> str:
        return self.name

    def get_all_tasks(self) -> List:
        return self.tasks
    
    def add_task(self, id, task_content) -> None:
        self.tasks.append(Task(id, task_content))
    
