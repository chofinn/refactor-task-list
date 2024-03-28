import sys
from task_list_app.io.console import Console
from task_list_app.io.app import TaskListApp

def main():
    task_list = TaskListApp(Console(sys.stdin, sys.stdout))
    task_list.run()

if __name__ == "__main__":
    main()