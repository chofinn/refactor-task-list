import sys

from task_list_app.console import Console
from task_list_app.app import TaskList


def main():
    task_list = TaskList(Console(sys.stdin, sys.stdout))
    task_list.run()


if __name__ == "__main__":
    main()

