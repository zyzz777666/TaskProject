import time


class TaskTracker:
    data = {}

    @classmethod
    def add(cls, task: str):
        for id in range(len(cls.data) + 1):
            if str(id) not in cls.data:
                cls.data[str(id)] = {'task': task,
                                     'createdAt': time.ctime()}

                print(f'Задача добавлена ее ID({id})')

    @classmethod
    def update(cls, id, task):
        if str(id) not in cls.data:
            raise 'Такой таски не сущесвует'
        cls.data[str(id)]['task'] = task
        cls.data[str(id)]['updatedAt'] = time.ctime()

    @classmethod
    def delete(cls, id):
        if str(id) not in cls.data:
            raise 'Такой таски не сущесвует'
        del cls.data[str(id)]

    @classmethod
    def show_all_tasks(cls, data: dict):
        if len(data) == 0:
            raise 'У вас нет задач'
        for task in data:
            print(f'ID[{task}]: {data[task]}')
            print()

    @classmethod
    def show_all_done_tasks(cls, data):
        if len(data) == 0:
            raise 'У вас нет задач'
        for task in data:
            if data[task]['status'] == 'завершено':
                print(f'ID[{task}]: {data[task]}')
                print()

    @classmethod
    def show_all_not_done_tasks(cls, data):
        if len(data) == 0:
            raise 'У вас нет задач'
        for task in data:
            if data[task]['status'] == '':
                print(f'ID[{task}]: {data[task]}')
                print()

    @classmethod
    def show_all_in_progress_done_tasks(cls, data):
        if len(data) == 0:
            raise 'У вас нет задач'
        for task in data:
            if data[task]['status'] == 'в процессе':
                print(f'ID[{task}]: {data[task]}')
                print()

    @classmethod
    def status(cls, id: str, status: str):
        status_in_progress = 'IN_PROGRESS'
        status_done = 'DONE'

        if id not in cls.data:
            raise ValueError
        if status == status_in_progress:
            cls.data[str(id)]['status'] = 'в процессе'
        elif status == status_done:
            cls.data[str(id)]['status'] = 'завершено'
