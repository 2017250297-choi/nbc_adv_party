import threading
from multi_process import Process
import os


def foo():
    print('=== Me foo. Me do task A. ===')
    print(f'thread id: {threading.get_native_id()}')
    print(f'pid is:    {os.getpid()}')


def bar():
    print('=== Me bar. Me do task B. ===')
    print(f'thread id: {threading.get_native_id()}')
    print(f'pid is:    {os.getpid()}')


def baz():
    print('=== Me baz. Me do task C. ===')
    print(f'thread id: {threading.get_native_id()}')
    print(f'pid is:    {os.getpid()}')


def foobarbaz():
    print('----------child process start----------')
    print(f'Im process. My pid is {os.getpid()}')
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()

    print('-----------child process end-----------')


if __name__ == '__main__':
    print(f'Im process. My pid is {os.getpid()}')
    # threds do same taskts on child process
    child = Process(target=foobarbaz).start()
    # threads do different tasks
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()
