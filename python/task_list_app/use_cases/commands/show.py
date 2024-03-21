from .command_interface import CommandInterface

class ShowCommand(CommandInterface):
    def __init__(self, task_list) -> None:
        self.task_list = task_list

    def execute(self, command: str=None) -> None:
        result = ""
        for project in self.task_list.get_all_projects():
            result += project.get_name() + "\n"
            for task in project.get_all_tasks():
                result += f"  [{'x' if task.is_done() else ' '}] {task.id}: {task.description}\n"
            result += "\n"
        return result