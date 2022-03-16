"""Race conditions can occur when two or more threads access a shared piece of data or resource."""
import concurrent.futures
import logging
import time
import threading

# Race condition example
# class FakeDatabase:
#     def __init__(self):
#         self.value = 0

#     def update(self, name):
#         logging.info("Thread %s: starting update", name)
#         local_copy = self.value
#         local_copy += 1
#         time.sleep(0.1)
#         self.value = local_copy
#         logging.info("Thread %s: finishing update", name)

# Preventing race condition with Lock
class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)

        # if used with `with` statement there's no need to use .acquire() and .release() 
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)

        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level=logging.DEBUG,
    #                     datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(database.locked_update, range(2))
        # for index in range(2):
        #     executor.submit(database.locked_update, index)
    logging.info("Testing update. Ending value is %d.", database.value)

"""Deadlock.
When the program calls l.acquire() the second time, it hangs waiting for the Lock to be released.
In this example, you can fix the deadlock by removing the second call, but deadlocks usually happen from one of two subtle things:
    1. An implementation bug where a Lock is not released properly
    2. A design issue where a utility function needs to be called by functions that might or might not already have the Lock

Always use context maanger in order to not forget to call release for each thread activation.
"""
# import threading

# # this is a deadlock. To fix uncomment release for each call to acquire()
# l = threading.RLock() # if RLock is used, we can stack acquire() call nut still have  to acll release same time as we call acquire()
# print("before first acquire")
# l.acquire()
# print("before second acquire")
# # l.release()

# l.acquire()
# print("acquired lock twice")
# l.release()
# l.release()


# print("working")
