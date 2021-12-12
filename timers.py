import time
from threading import Timer


def display(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'))


def run_once():
    display('run_once:')
    t = Timer(5, display, ['Timeout!!'])
    t.start()


run_once()
print('waiting...')
