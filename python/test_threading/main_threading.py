import threading
from time import ctime ,sleep
import logging

logging.basicConfig(level=logging.INFO)

test=[2,4]

def test1(name,sleep_time):
    logging.info("start loop " +str(name) + " at " + ctime())
    sleep(sleep_time)
    logging.info("end loop " +str(name) + "at " + ctime())


def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(test))
    for i in nloops:
        t = threading.Thread(target=test1,args=(i,test[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())

if __name__ =="__main__":
    main()