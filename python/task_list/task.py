

class Task:
    def __init__(self, id_: int, description: str, done: bool) -> None:
        self.id = id_
        self.description = description
        self.done = done

    def set_done(self, id_string: str, done: bool) -> None:
        id_ = int(id_string)
        for project, tasks in self.tasks.items():
            for task in tasks:
                if task.id == id_:
                    self.done = done
                    return
        self.console.print(f"Could not find a task with an ID of {id_}")
        self.console.print()
        
    def is_done(self) -> bool:
        return self.done

