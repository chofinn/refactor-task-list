from typing import Dict, List
from task_list.project import Project

class TaskList:
    def __init__(self) -> None:
        self.projects = []
        self.id = 1

    def get_project(self, prj_name: str) -> Project:
        for prj in self.projects:
            if prj.get_name() == prj_name:
                return prj
        return None
    
    def get_all_projects(self) -> List:
        return self.projects
    
    # maybe this three should not be here?
    def add_project(self, prj_name):
        self.projects.append(Project(prj_name))

    def add_task(self, prj_name, task_content) -> None:
        project = self.get_project(prj_name)
        if project == None:
            return
            # FIXME: find out how to handle error
        project.add_task(self.id, task_content)
        self.id += 1
    
    def set_state(self, id, state: bool):
        for prj in projects:
            # tbd
            pass