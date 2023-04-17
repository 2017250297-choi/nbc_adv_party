import threading
import os


def foo():
    print('=== Me foo. Me do task A. ===')
    print(f'thread id: {threading.get_native_id()}')
    print(f'pid is:    {os.getpid()}')


if __name__ == '__main__':
    print(f'Im process. My pid is {os.getpid()}')
    # threads do a same task
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()
