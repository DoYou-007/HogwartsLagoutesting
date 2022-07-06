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

def main():
    logging.info("start all at " + ctime())
    test1()
    test2()
    sleep(6)
    logging.info("end all at " + ctime())

if __name__ =="__main__":
    main()
