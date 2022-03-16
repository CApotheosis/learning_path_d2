"""
threading.get_ident() returns a unique name for each thread, but these are usually neither short nor easily readable.

In computer science, a daemon is a process that runs in the background.
In python a daemon thread will shut down immediately when the program exits. 
"""
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # logging.info("Main    : before creating thread")
    # # with daemon flag set to True, the program won't wait for func to execute
    # x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    # logging.info("Main    : before running thread")
    # x.start()
    # logging.info("Main    : wait for the thread to finish")
    # # To tell one thread to wait for another thread to finish, you call .join(). 
    # x.join() # Wait until the thread terminates. Works despite setting deamon to True
    # logging.info("Main    : all done")

    # multiple threads
    # threads = list()
    # for index in range(3):
    #     logging.info("Main    : create and start thread %d.", index)
    #     x = threading.Thread(target=thread_function, args=(index,))
    #     threads.append(x)
    #     x.start()

    # for index, thread in enumerate(threads):
    #     logging.info("Main    : before joining thread %d.", index)
    #     thread.join()
    #     logging.info("Main    : thread %d done", index)

import concurrent.futures
import os

print(os.cpu_count())
# [rest of code]

if __name__ == "__main__":
    """
    The code creates a ThreadPoolExecutor as a context manager, telling it how many worker threads it wants in the pool. 
    It then uses .map() to step through an iterable of things, in your case range(3), passing each one to a thread in the pool.
    ThreadPoolExecutor with `with` calls join 
    """
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(thread_function, range(3))
