import _thread
from time import ctime ,sleep
import logging

logging.basicConfig(level=logging.INFO)

def test1():
    logging.info("start test1 at " + ctime())
    sleep(4)
    logging.info("end test1 at " + ctime())


def test2():
    logging.info("start test2 at " + ctime())
    sleep(2)
    logging.info("end test2 at " + ctime())

#不添加锁的情况下，需要添加sleep进行等待子线程结束，否则主进程结束后子线程也会结束
# def main():
#     logging.info("start all at " + ctime())
#     _thread.start_new_thread(test1,())
#     _thread.start_new_thread(test2,())
#     sleep(6)
#     logging.info("end all at " + ctime())

def main():
    logging.info("start all at " + ctime())
    _thread.start_new_thread(test1,())
    _thread.start_new_thread(test2,())
    sleep(6)
    logging.info("end all at " + ctime())

if __name__ =="__main__":
    main()