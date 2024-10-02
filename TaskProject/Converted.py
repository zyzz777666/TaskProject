from Tracker import TaskTracker
import json


class Convert:
    @staticmethod
    def dict_converted_to_json(file):
        with open(file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(TaskTracker.data, ensure_ascii=False))

    @staticmethod
    def json_converted_to_dict(file):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                TaskTracker.data = json.load(f)
        except json.JSONDecodeError:
            Convert.dict_converted_to_json('task.json')
