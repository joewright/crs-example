import json
from tasks import my_cool_task
from time import sleep


def do_stuff():
    print('calling the task')
    my_cool_task.apply_async(args=[json.dumps({'it_worked': True})])
    sleep(5)
    do_stuff()

if __name__ == '__main__':
    do_stuff()
