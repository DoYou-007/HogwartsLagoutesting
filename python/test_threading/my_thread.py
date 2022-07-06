import threading
from time import ctime ,sleep
import logging

logging.basicConfig(level=logging.INFO)

class Mythread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        self.func(*self.args)

test=[2,4]

def test1(name,sleep_time):
    logging.info("start loop " +str(name) + " at " + ctime())
    sleep(sleep_time)
    logging.info("end loop " +str(name) + " at " + ctime())


def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(test))
    for i in nloops:
        t = Mythread(test1,(i,test[i]),test1.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())

if __name__ =="__main__":
    main()