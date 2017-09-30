
import threading
import time


class MyThread(threading.Thread):

    def __init__(self, name, id, counter):
        threading.Thread.__init__(self)
        self.name = name
        self.id = id
        self.counter = counter

    def run(self):
        print(self.name, self.id, "Started")
        thredlock.acquire()
        print_time(self.name, self.counter, 3)
        thredlock.release()


def print_time(name, delay, counter):
    while counter:
        time.sleep(delay)
        print(name, time.ctime(time.time()))
        counter -=1


thredlock = threading.Lock()
threads = []

thread1 = MyThread("thread-1", 1, 1)
thread2 = MyThread("thread-2", 2, 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

# wait for the threads to finish
for t in threads:
    t.join()

print("Exiting Main Thread")