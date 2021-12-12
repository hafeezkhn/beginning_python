#imports and globals
import os
stats = dict(path='', folders=0, files=0, links=0, size=0)
# get user inputs


def get_input():
    global stats
    ret = os.path.abspath(input("enter the path"))
    if not os.path.exists(ret):
        print('dorry that not exist')
        exit(1)
    if not os.path.isdir(ret):
        print('dorry that not directory')
        exit(2)

    stats['path'] = ret

# scan path recursively


def scan(path):
    global stats
    print('scanning: ' + path)
    for root, dirs, files in os.walk(path, onerror=None, followlinks=False):
        stats['folders'] += len(dirs)
        stats['files'] += len(dirs)
        for name in files:
            fullname = os.path.join(root, name)
            size = os.path.getsize(fullname)
            stats['size'] += size

# display


def display():
    global stats
    print('Resuts:')
    for k, v in stats.items():
        print(f'{k} = {v}')

# main


def main():
    global stats
    get_input()
    scan(stats['path'])
    display()


if __name__ == "__main__":
    main()
