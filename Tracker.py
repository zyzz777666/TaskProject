import json


class TaskTracker:
    data = {}

    @staticmethod
    def add(task: str):
        for id in range(len(TaskTracker.data) + 1):
            if str(id) not in TaskTracker.data:
                TaskTracker.data[str(id)] = task

    @staticmethod
    def update(id, task):
        if str(id) not in TaskTracker.data:
            raise 'Такой таски не сущесвует'
        TaskTracker.data[str(id)] = task

    @staticmethod
    def delete(id):
        if str(id) not in TaskTracker.data:
            raise 'Такой таски не сущесвует'
        del TaskTracker.data[str(id)]

    @staticmethod
    def show_all_tasks(tasks: dict) -> list:
        if len(TaskTracker.data) == 0:
            raise 'У вас нет задач'
        print([_ for _ in tasks.values()])