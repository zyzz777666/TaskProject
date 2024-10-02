import time


class TaskTracker:
    data = {}

    @staticmethod
    def add(task: str):
        for id in range(len(TaskTracker.data) + 1):
            if str(id) not in TaskTracker.data:
                TaskTracker.data[str(id)] = {'task': task,
                                             'status': '',
                                             'time': time.ctime()}
                print(f'Задача добавлена ее ID({id})')

    @staticmethod
    def update(id, task):
        if str(id) not in TaskTracker.data:
            raise 'Такой таски не сущесвует'
        TaskTracker.data[str(id)] = {'task': task,
                                     'status': '',
                                     'time': time.ctime()}

    @staticmethod
    def delete(id):
        if str(id) not in TaskTracker.data:
            raise 'Такой таски не сущесвует'
        del TaskTracker.data[str(id)]

    @staticmethod
    def show_all_tasks(data: dict):
        if len(data) == 0:
            raise 'У вас нет задач'
        for i in data:
            print(f'ID[{i}]: {data[i]}')
            print()

    @staticmethod
    def show_all_done_tasks(data):
        if len(data) == 0:
            raise 'У вас нет задач'
        for i in data:
            if data[i]['status'] == 'завершено':
                print(f'ID[{i}]: {data[i]}')
                print()

    @staticmethod
    def show_all_not_done_tasks(data):
        if len(data) == 0:
            raise 'У вас нет задач'
        for i in data:
            if data[i]['status'] == '':
                print(f'ID[{i}]: {data[i]}')
                print()

    @staticmethod
    def show_all_in_progress_done_tasks(data):
        if len(data) == 0:
            raise 'У вас нет задач'
        for i in data:
            if data[i]['status'] == 'в процессе':
                print(f'ID[{i}]: {data[i]}')
                print()

    @staticmethod
    def status(id: str, status: str):
        status_in_progress = 'IN_PROGRESS'
        status_done = 'DONE'

        if id not in TaskTracker.data:
            raise ValueError
        if id not in TaskTracker.data:
            raise 'Такой таски не сущесвует'
        if status == status_in_progress:
            TaskTracker.data[str(id)]['status'] = 'в процессе'
            TaskTracker.data[str(id)]['time'] = time.ctime()
        elif status == status_done:
            TaskTracker.data[str(id)]['status'] = 'завершено'
            TaskTracker.data[str(id)]['time'] = time.ctime()