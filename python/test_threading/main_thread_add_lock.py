import _thread
from time import ctime ,sleep
import logging

logging.basicConfig(level=logging.INFO)

test=[2,4]

def test1(name,sleep_time,lock):
    logging.info("start loop " +str(name) + " at " + ctime())
    sleep(sleep_time)
    logging.info("end loop " +str(name) + "at " + ctime())
    lock.release()


def main():
    logging.info("start all at " + ctime())
    locks = []
    nloops = range(len(test))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(test1,(i,test[i],locks[i]))
    for i in nloops:
        while locks[i].locked():pass
    logging.info("end all at " + ctime())

if __name__ =="__main__":
    main()