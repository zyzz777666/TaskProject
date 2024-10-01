import argparse
import Converted
import Tracker
import sys


def main():
    parser = argparse.ArgumentParser(description="CLI-Task Tracker приложение на Python",
                                     prog="Task Tracker")


if __name__ == "__main__":
    Converted.Convert.json_converted_to_dict('task.json')
    Tracker.TaskTracker.add('dasfwqeqwr')
    Converted.Convert.dict_converted_to_json('task.json')
    main()
