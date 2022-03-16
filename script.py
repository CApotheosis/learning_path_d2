from tkinter import E


def func(o):
    try:
        o["a"] = 1/0
    except Exception as err:
        print(err)

o = {"a": 1, "b": 1}
d = {}
d = func(o)

print(o)


class A:
    def process(self):
        print('A process()')


class B(A):
    def process(self):
        print('B process()')


# class C(A, B):
#     def mro(self):
#         return [C, A, B, object]

# obj = C()
# obj.mro()
# obj.process()

a, *_, b = 1,2,3,4,5
print(a, b, *_)


def func(c):
    print(c)


func("dsadasd", **{})

def num(*args):
    print(args)

num(1, 2, 3, 4)

import pydantic
print('compiled:', pydantic.compiled)


q = lambda: locals()
print(q())

def func():
    qwerty = 1
    print(locals())
    print(globals())

# func()

import logging
import os
from queue import Queue
from threading import Thread
from time import time

# from download import setup_download_dir, get_links, download_link


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


class DownloadWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self) # we extended Thread class to DownloadWorker
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            directory, link = self.queue.get()
            try:
                download_link(directory, link)
            finally:
                self.queue.task_done()

queue = Queue()
download = DownloadWorker(queue)
print(download, download.queue)
print(Thread.__init__())
