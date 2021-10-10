import threading
import time
import queue

class tT:

    def __init__(self):

        self.timer = time
        self.lock = threading.Lock()

    def abc(self):

        a = 1
        for i in range(10):

            self.lock.acquire()
            a = a+1
            print("thread:"+str(a))
            self.timer.sleep(1)
            self.lock.release()

    def abc2(self, b, c):

        b = 10
        for i in range(5):

            self.lock.acquire()
            b = b-1
            print("thread2:"+str(b))
            self.timer.sleep(1)
            self.lock.release()

    def abc3(self):

        c = 2
        for i in range(15):

            self.lock.acquire()
            c = c+5
            print("thread3:"+str(c))
            self.timer.sleep(1)
            self.lock.release()

    def test(self):

        t1 = threading.Thread(target=self.abc)
        t2 = threading.Thread(target=self.abc2, args=(0, 1))
        t3 = threading.Thread(target=self.abc3)

        t1.start()
        t1.join()
        t2.start()
        t2.join()
        t3.start()
t = tT()
main = t.test()