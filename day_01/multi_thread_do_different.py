import threading
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


if __name__ == '__main__':
    print(f'Im process. My pid is {os.getpid()}')
    # threads do different tasks
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()
