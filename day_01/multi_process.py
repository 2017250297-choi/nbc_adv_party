from multiprocessing import Process
import os
############################
##### Multi-Processing #####
############################


def func1():
    print()
    print('=====this is f1=====')
    print('=== I do task AA ===')
    print('my pid', os.getpid())
    print('my parents pid', os.getppid())


def func2():
    print()
    print('=====this is f2=====')
    print('=== I do task BB ===')
    print('my pid', os.getpid())
    print('my parents pid', os.getppid())


def func3():
    print()
    print('=====this is f3=====')
    print('=== I do task CC ===')
    print('my pid', os.getpid())
    print('my parents pid', os.getppid())


if __name__ == '__main__':
    print('python root pid is', os.getpid())
    # different processes do a same task
    changsu1 = Process(target=func1).start()
    changsu2 = Process(target=func1).start()
    changsu3 = Process(target=func1).start()
    # different processes do different tasks
    changsu1 = Process(target=func1).start()
    changsu2 = Process(target=func2).start()
    changsu3 = Process(target=func3).start()
