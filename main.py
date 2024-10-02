import argparse
import Converted
import Tracker
import click


@click.command()
def main():
    start = int(input('Введите 1 что бы начать: '))
    if start == 1:
        Converted.Convert.json_converted_to_dict('task.json')

        while True:

            command = input("""
            Введите add что бы добавить таску
            Введите update что бы изменить таску
            Введите del что бы удалить таску
            Введите show что бы показать все таски
            Введите todo что бы отметить таску
            Введите done что бы вывести завершенные задачи
            Введите not что бы вывести не завершенные задачи
            Введите progress что бы вывести все задачи в прогрессе
            Введите quit что бы завершить и сохранить данные
            Введите save что бы сохранить данные: """)
            print()
            print()

            if command == 'add':
                Tracker.TaskTracker.add(input('Введите таску: '))
            elif command == 'update':
                Tracker.TaskTracker.update(input('Введите id таски: '), input('Введите таску: '))
            elif command == 'del':
                Tracker.TaskTracker.delete(input('Введите id таски: '))
            elif command == 'show':
                Tracker.TaskTracker.show_all_tasks(Tracker.TaskTracker.data)
            elif command == 'todo':
                Converted.Convert.json_converted_to_dict('task.json')
                try:
                    Tracker.TaskTracker.status(input('Введите id таски: '),
                                               input('Введите "IN_PROGRESS" или "DONE"').upper())
                except ValueError:
                    print('Такой таски не сущесвует')
                Converted.Convert.dict_converted_to_json('task.json')
            elif command == 'done':
                Tracker.TaskTracker.show_all_done_tasks(Tracker.TaskTracker.data)
            elif command == 'not':
                Tracker.TaskTracker.show_all_not_done_tasks(Tracker.TaskTracker.data)
            elif command == 'progress':
                Tracker.TaskTracker.show_all_in_progress_done_tasks(Tracker.TaskTracker.data)
            elif command == 'save':
                Converted.Convert.dict_converted_to_json('task.json')
                click.echo('Данные успешно сохранены')
            elif command == 'quit':
                Converted.Convert.dict_converted_to_json('task.json')
                break


if __name__ == "__main__":
    main()
