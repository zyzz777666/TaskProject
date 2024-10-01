import argparse
import Converted
import Tracker



def main():
    parser = argparse.ArgumentParser(description="CLI-Task Tracker приложение на Python",
                                     prog="Task Tracker")


if __name__ == "__main__":
    Converted.Convert.json_converted_to_dict('task.json')
    Tracker.TaskTracker.show_all_tasks(Tracker.TaskTracker.data)
    Converted.Convert.dict_converted_to_json('task.json')
