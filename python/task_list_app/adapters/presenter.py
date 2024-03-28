class Presenter:
    def __init__(self, console) -> None:
        self.console = console

    def present(self, output: str):
        if output:
            self.console.print(output)