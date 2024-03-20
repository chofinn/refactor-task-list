class Task:
    def __init__(self, id_: int, description: str) -> None:
        self.id = id_
        self.description = description
        self.done = False

    def set_state(self, is_done: bool) -> None:
        self.done = is_done
        
    def is_done(self) -> bool:
        return self.done
    
    def get_id(self):
        return self.id

